# FreeSharedCockpit
An open source free XPlane 11 Shared cockpit plugin development 

Hi Guys,

I’m trying to develop a free and open source shared cockpit software that works with XP11. I have written my own python script to synchronise Xplane Datarefs across 2 computers over UDP protocol.

I know that there are alternatives out there for shared cockpit already, and the reason why I am doing this is because:
1) JoinFS doesn't work for shared cockpit on XPlane 11, trust me, I've tried everything to make it work...
2) Smartcopilot is way too expensive for single license
3) Teamviewer and Discord Screenshare does not provide a shared cockpit experience
4) An open source, free for all shared cockpit software that allows customisation would allow much more people to benefit from it, without paying a single cent.

The main target group of people that this program would potentially benefit are:
1) Folks who play XPlane offline, but are too scared to go on VATSIM online. Flying shared cockpit where the instructor and student are in the same plane will allow splitting of the workload, making it a less daunting task - I would certainly love to have an instructor with me on my first VATSIM flight!
2) Folks who are training for their VATSIM P ratings - discord screenshare or teamviewer is just inferior to a shared cockpit environment
3) Folks who just want to have fun flying together in a crew

An XPlane shared cockpit software is essentially a piece of software that syncs Xplane datarefs between 2 computers, such that moving the controls/switches on one computer causes a synchronised change on the other. 

As can be seen in the video below:

https://youtu.be/luqvsnya1GA

A big step forward now compared to the previous, aircraft attitude, heading and position are now synced exactly from master to slave. Again, the same setup, the laptop on the left is the slave computer, having the plane mirrored to the master Desktop on the right. Both sceneries look different because my laptop can only run on minimal settings while my desktop is running on high and you can see the ground features much better. 

Next steps would be to:
1) Sync the aircraft position velocity of XYZ and rotational velocity PQR
2) Allow toggle of control inputs between master and slave, the toggle button (on the master computer) should:
- Slave: Enable the physics model
- Master: Disable the physics model
- Slave: Stop setting aircraft position, attitude, velocities from the master 
- Master: Set aircraft position, attitude, velocities from the slave
3) Untoggling the switch should perform the above but in reverse
4) Create a GUI for the toggle button, Slave/Master IP address and Ports input box, connect button
5) Sync the engine on/off state 
6) Sync the cockpit/autopilot switches
7) Optimise for speed - cut down precision of variables, code cleanup
8) Write an instruction manual - required dependencies etc...

>>> Once we reach this stage, it will be time to publish an early beta of the software!



How to use:
1) Edit both files FreeSharedCockpitUDPSenderMaster.py and FreeSharedCockpitUDPSenderSlave.py and change the ip address of the "host" variable to the IP address of the other computer you are trying to connect to. (i.e: Master should input the slave's IP and Slave should input the Master's IP)
2) The PI_FreeSharedCockpit_pluginMaster.py script is to be placed in the PythonScripts folder under Xplane plugins folder on the Master computer, and the corresponding PI_FreeSharedCockpit_pluginSlave.py in the Xplane plugins folder on the Slave computer. 
3) Run the FreeSharedCockpitUDPSenderMaster.py script using the command line on the master computer and FreeSharedCockpitUDPSenderSlave.py on the slave computer.
4) Load up Xplane on both master and slave at same airport (does not need to be the exact same location at the airport) and make sure that both have the exact same scenery
5) On the slave computer, click on the dialog box once to start syncing the position of the slave to the master computer, the state of the aircraft on the slave computer will snap to reflect that on the master computer. Click the dialog box again to unsync.
6) Start flying on the master computer, the aircraft on the slave computer will be synced!



Anyone keen to help me in this project please feel free to contribute! Thanks for viewing!
