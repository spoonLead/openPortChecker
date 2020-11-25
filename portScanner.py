import socket
import sys


def portScanner():
    hostIP, maxPort = getHostIpAndMaxPort()
    printHostIpAndPortRange(hostIP, maxPort)


    for port in range(1,1024):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1000)
            s.connect(('127.0.0.1', port))
            print(port)
            s.close
        except: continue

def getHostIpAndMaxPort():
    hostIP = '127.0.0.1'
    maxPort = 1024
    if(getArgvLength() >= 2):
        hostIP = getHostIPFromArgv()
    if(getArgvLength() >= 3):
        maxPort = getmaxPortnFromArgv()
    return(hostIP,maxPort)

def getArgvLength():
    return(len(sys.argv))

def getHostIPFromArgv():
    return(sys.argv[1])

def getmaxPortnFromArgv():
    return(sys.argv[1])


def printHostIpAndPortRange(hostIP, maxPort):
    print("Host IP: " + str(hostIP))
    print("Ports range: (0 - " + str(maxPort) + ")")


portScanner()
