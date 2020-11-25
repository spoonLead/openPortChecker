#TODO: multithreading
#TODO: writing open ports and hostIp to file

import socket
import sys


def portScanner():
    global HOST_IP
    global MAX_PORT

    HOST_IP, MAX_PORT = getHostIpAndMaxPort()
    printHostIpAndPortRange()
    scanPorts()


def getHostIpAndMaxPort():
    hostIP = '127.0.0.1'
    maxPort = 1024
    if(getArgvLength() >= 2):
        hostIP = getHostIPFromArgv()
    if(getArgvLength() >= 3):
        maxPort = getMaxPortFromArgv()
    return(hostIP,maxPort)

def getArgvLength():
    return(len(sys.argv))

def getHostIPFromArgv():
    return(sys.argv[1])

def getMaxPortFromArgv():
    return(int(sys.argv[2]))


def printHostIpAndPortRange():
    print("Host IP: " + str(HOST_IP))
    print("Ports range: (0 - " + str(MAX_PORT) + ")")


def scanPorts():
    print("\nScanning in progress")
    print("Open TCP ports:")
    for port in range(1,MAX_PORT):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST_IP, port))
            print("Открытый порт: " + str(port))
            sock.close
        except: continue
    print("The scan is complete")

portScanner()
