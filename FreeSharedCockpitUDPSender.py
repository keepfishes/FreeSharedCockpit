import socket
import pickle
import threading

host = '192.168.1.115'
inip = '0.0.0.0'
inport = 49001
outport = 49000

def udpRx():
    while 1:
        try:
            infile = open('C:/1.fll', 'r')
            PickledTx = infile.read()
        except:
            print('read error')

        s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s1.connect((host, outport), )
        s1.sendto(PickledTx, (host, outport))
        s1.close()

        s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s2.settimeout(0.04)
        try:
            s2.bind((inip, inport), )
            PickledRx = s2.recvfrom(1024)
            try:
                outfile = open('C:/2.fll', 'w')
                outfile.write(PickledRx[0])
                print(PickledRx[0])
            except:
                print('Unable to write')
        except(socket.timeout, IndexError):
            print('UDP no data received from Port: ' + str(inport))
        s2.close()


udpthread = threading.Thread(target=udpRx).start()  # export data and receive data every cycle

