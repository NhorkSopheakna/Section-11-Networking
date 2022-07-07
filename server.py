import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50005
sock.connect (('172.16.1.96', port))
msg = sock.recv(1024)
msg

msg_decoded = msg.decode('utf_8')
msg_decoded

print('Message From Server: ' + msg_decoded)

msg_back = input('Do you Want To The Server ?')
msg_back_encoded = msg_back.encode('utf-8')
sock.send(msg_back_encoded)

