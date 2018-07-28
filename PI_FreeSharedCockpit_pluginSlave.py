from XPLMDefs import *
from XPLMDataAccess import *
from XPLMDisplay import *
from XPLMGraphics import *
from XPLMUtilities import *
import pickle
import os

DataRx = []
sync = False

filename = 'C:/2.fll'
try:
    os.remove(filename)
except OSError:
    print('Cant remove file!')

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
        
        # Access in sim variables
        AccessorDataRefX = XPLMFindDataRef("sim/flightmodel/position/local_x")
        DataX = XPLMGetDataf(AccessorDataRefX)
        AccessorDataRefY = XPLMFindDataRef("sim/flightmodel/position/local_y")
        DataY = XPLMGetDataf(AccessorDataRefY)
        AccessorDataRefZ = XPLMFindDataRef("sim/flightmodel/position/local_z")
        DataZ = XPLMGetDataf(AccessorDataRefZ)
        AccessorDataRefPsi = XPLMFindDataRef("sim/flightmodel/position/psi")
        DataPsi = XPLMGetDataf(AccessorDataRefPsi)
        AccessorDataRefTheta = XPLMFindDataRef("sim/flightmodel/position/theta")
        DataTheta = XPLMGetDataf(AccessorDataRefTheta)
        AccessorDataRefPhi = XPLMFindDataRef("sim/flightmodel/position/phi")
        DataPhi = XPLMGetDataf(AccessorDataRefPhi)
        AccessorDataRefP = XPLMFindDataRef("sim/flightmodel/position/P")
        DataP = XPLMGetDataf(AccessorDataRefP)
        AccessorDataRefQ = XPLMFindDataRef("sim/flightmodel/position/Q")
        DataQ = XPLMGetDataf(AccessorDataRefQ)
        AccessorDataRefR = XPLMFindDataRef("sim/flightmodel/position/R")
        DataR = XPLMGetDataf(AccessorDataRefR)
        AccessorDataRefVX = XPLMFindDataRef("sim/flightmodel/position/local_vx")
        DataVX = XPLMGetDataf(AccessorDataRefVX)
        AccessorDataRefVY = XPLMFindDataRef("sim/flightmodel/position/local_vy")
        DataVY = XPLMGetDataf(AccessorDataRefVY)
        AccessorDataRefVZ = XPLMFindDataRef("sim/flightmodel/position/local_vz")
        DataVZ = XPLMGetDataf(AccessorDataRefVZ)

        # Export in sim data to other comp
        global DataRx
        DataTx = [DataX, DataY, DataZ, DataPsi, DataTheta, DataPhi, DataP, DataQ, DataR, DataVX, DataVY, DataVZ]
        outfile = open('C:/1.fll', 'w')
        pickle.dump(DataTx, outfile)
        outfile.close()

        try:
            infile = open('C:/2.fll', 'r')
            DataRx = pickle.load(infile)
        except:
            pass

        # Slave specific script
        # Sync the position of the slave to the master when box is clicked
        if self.Clicked:
            global sync
            sync = not sync
            print(sync)
            if sync == False:
                PhysicsRef = XPLMFindDataRef("sim/operation/override/override_planepath")
                ovrd_Vals = [0]
                XPLMSetDatavi(PhysicsRef, ovrd_Vals, 0, 1)

        if sync == True:
            try:
                PhysicsRef = XPLMFindDataRef("sim/operation/override/override_planepath")
                ovrd_Vals = [1]
                XPLMSetDatavi(PhysicsRef, ovrd_Vals, 0, 1)
                XPLMSetDataf(AccessorDataRefX, DataRx[0])
                XPLMSetDataf(AccessorDataRefY, DataRx[1])
                XPLMSetDataf(AccessorDataRefZ, DataRx[2])
                XPLMSetDataf(AccessorDataRefPsi, DataRx[3])
                XPLMSetDataf(AccessorDataRefTheta, DataRx[4])
                XPLMSetDataf(AccessorDataRefPhi, DataRx[5])
                XPLMSetDataf(AccessorDataRefP, DataRx[6])
                XPLMSetDataf(AccessorDataRefQ, DataRx[7])
                XPLMSetDataf(AccessorDataRefR, DataRx[8])
                XPLMSetDataf(AccessorDataRefVX, DataRx[9])
                XPLMSetDataf(AccessorDataRefVY, DataRx[10])
                XPLMSetDataf(AccessorDataRefVZ, DataRx[11])
                
            except:
                pass
        else:
            pass



        # Common script for both master and slave
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
