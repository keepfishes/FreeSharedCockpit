# FreeSharedCockpit
An open source free XPlane 11 Shared cockpit plugin development 

Hi Guys,

I’m trying to develop a free and open source shared cockpit software that works with XP11. I have written my own python script to synchronise Xplane Datarefs across 2 computers over UDP protocol.

I know that there are some available options out there for shared cockpit already, and the reason why I am doing this is because:

1) JoinFS doesn't work for shared cockpit on XPlane 11, trust me, I've tried everything to make it work...

2) Smartcopilot is way too expensive for single license

3) Teamviewer and Discord Screenshare does not provide a shared cockpit experience

4) An open source, free for all shared cockpit software that allows customisation would allow much more people to benefit from it, without paying a single cent. This is particularly useful for budding aviation enthusiasts that can't afford to spend extra and want to take lessons from online instructors e.g.: VATSIM ATOs but don't have a smart cockpit solution, which would make lessons so much easier and immersive if there were a shared cockpit.

An Xplane shared cockpit software is essentially a piece of software that syncs Xplane datarefs between 2 computers, such that moving the controls/switches on one computer causes a synchronised change on the other. 

The project as of now is at an early stage. I have tested it with LAN, and one computer is able to mirror the others' aircraft position in space. The next easy step would be to add more datarefs to be synchronised (aicraft attitude, heading and instruments).

As can be seen in the video below:

https://youtu.be/SLPtdesNDvw

The laptop on the left is the slave, and is getting its position synced from the desktop. The command box that you see scrolling thru with all the numbers on the right is showing all the datarefs that are being sent to the other computer.

So far I’ve managed to turn off the physics engine, to allow the desktop to manipulate the plane on the laptop to synchronise the X, Y and Z positions on the laptop. Next will be to synchronise the datarefs for heading and engine and cockpit switches.

Once that is done, it will be a big step forward to realising a free shared cockpit software for Xplane that actually works!

The first file PI_FreeSharedCockpit_plugin.py is meant to be placed in the PythonScripts folder in the plugins folder in the Xplane directory (with Sandy's PythonInterface plugin installed). This script extracts datarefs from Xplane and writes it to a file on C drive. The second python script FreeSharedCockpitUDPSender.py uses the pickled data in the file and sends it over UDP to the other network computer via ports 49000 and 49001, and also receives incoming data from the other computer, and feeds it back to the PI_FreeSharedCockpit_plugin.py plugin, which then effects a change in Xplane.

Anyone keen to help me in this project please feel free to contribute!
