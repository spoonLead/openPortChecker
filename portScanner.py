import socket

for port in range(1,1024):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1000)
        s.connect(('127.0.0.1', port))
        print(port)
        s.close
    except: continue
