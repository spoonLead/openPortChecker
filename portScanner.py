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
        maxPort = getmaxPortnFromArgv()
    return(hostIP,maxPort)

def getArgvLength():
    return(len(sys.argv))

def getHostIPFromArgv():
    return(sys.argv[1])

def getmaxPortnFromArgv():
    return(sys.argv[1])


def printHostIpAndPortRange():
    print("Host IP: " + str(HOST_IP))
    print("Ports range: (0 - " + str(MAX_PORT) + ")")


def scanPorts():
    print("\nScanning in progress")
    print("Open TCP ports:")
    for port in range(1,MAX_PORT):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1000)
            sock.connect((HOST_IP, port))
            print(port)
            sock.close
        except: continue
    print("The scan is complete")

portScanner()
