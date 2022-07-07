import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50005
sock.connect (('172.16.1.96', port))
msg = sock.recv(1024)
msg

