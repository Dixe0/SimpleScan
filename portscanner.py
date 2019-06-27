import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Change at host the target you want to scan
host = "111.11.111.11"
# Change at port the port you want to scan, its can 21 (FTP) 22 (SSH) etc.
port = 21

def portscanner(port):
    if sock.connect_ex((host, port)):
        print ("Port %d is close" % (port))
    else:
        print ("Port %d is opened" % (port))


portscanner(port)
