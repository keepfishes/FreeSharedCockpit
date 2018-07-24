from XPLMDefs import *
from XPLMDataAccess import *
from XPLMDisplay import *
from XPLMGraphics import *
from XPLMUtilities import *
import pickle

DataRx = []

class PythonInterface:

    def XPluginStart(self):
        self.Name = "Test"
        self.Sig =  "Ong.Python.Test"
        self.Desc = "Datarefs"
        self.Clicked = 0
        self.DrawWindowCB = self.DrawWindowCallback
        self.KeyCB = self.KeyCallback
        self.MouseClickCB = self.MouseClickCallback
        self.WindowId = XPLMCreateWindow(self, 50, 600, 400, 570, 1, self.DrawWindowCB, self.KeyCB, self.MouseClickCB, 0)
        return self.Name, self.Sig, self.Desc

    def XPluginStop(self):
        XPLMDestroyWindow(self, self.WindowId)
        pass

    def XPluginEnable(self):
        return 1

    def XPluginDisable(self):
        pass

    def XPluginReceiveMessage(self, inFromWho, inMessage, inParam):
        pass

    def DrawWindowCallback(self, inWindowID, inRefcon):
        # First we get the location of the window passed in to us.
        lLeft = [];	lTop = []; lRight = [];	lBottom = []
        XPLMGetWindowGeometry(inWindowID, lLeft, lTop, lRight, lBottom)
        left = int(lLeft[0]); top = int(lTop[0]); right = int(lRight[0]); bottom = int(lBottom[0])
        XPLMDrawTranslucentDarkBox(left, top, right, bottom)
        color = 1.0, 1.0, 1.0

        AccessorDataRefX = XPLMFindDataRef("sim/flightmodel/position/local_x")
        DataX = XPLMGetDataf(AccessorDataRefX)
        AccessorDataRefY = XPLMFindDataRef("sim/flightmodel/position/local_y")
        DataY = XPLMGetDataf(AccessorDataRefY)
        AccessorDataRefZ = XPLMFindDataRef("sim/flightmodel/position/local_z")
        DataZ = XPLMGetDataf(AccessorDataRefZ)

        global DataRx
        DataTx = [DataX, DataY, DataZ]
        outfile = open('C:/1.fll', 'w')
        pickle.dump(DataTx, outfile)
        outfile.close()
        try:
            infile = open('C:/2.fll', 'r')
            DataRx = pickle.load(infile)
        except:
            print('IOError')

        #if self.Clicked:
        XPLMSetDataf(AccessorDataRefX, DataRx[0])
        XPLMSetDataf(AccessorDataRefY, DataRx[1])
        XPLMSetDataf(AccessorDataRefZ, DataRx[2])
        PhysicsRef = XPLMFindDataRef("sim/operation/override/override_planepath")
        XPLMSetDatai(PhysicsRef, 0)

        DescTx = 'Tx: ' + str(DataTx)
        DescRx = 'Rx: ' + str(DataRx)
        XPLMDrawString(color, left + 5, top - 10, DescTx, 0, xplmFont_Basic)
        XPLMDrawString(color, left + 5, top - 20, DescRx, 0, xplmFont_Basic)
        pass

    def KeyCallback(self, inWindowID, inKey, inFlags, inVirtualKey, inRefcon, losingFocus):
        pass

    def MouseClickCallback(self, inWindowID, x, y, inMouse, inRefcon):
        if (inMouse == xplm_MouseDown) or (inMouse == xplm_MouseUp):
            self.Clicked = 1 - self.Clicked
        return 1
