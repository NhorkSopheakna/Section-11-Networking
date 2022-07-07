import socket
s = socket.socket(socket.Af_INET, socket.SOCK_STREAM)
s.bind(('172.16.1.96', 50005))
s.listen(5)
clientsocket,clientaddress = s.accept()
print(clientsocket)


clientaddress
print('Got a connection from %s' % str(clientaddress))
msg = input ('Enter Any Message: ')
msg_encoded = msg.encode('utf-8')
clientsocket.send(msg_encoded)

clientsocket.recv(1024)
message_back = clientsocket.recv(1024)
message_back_decoded = message_back.decode('utf-8')
print('Response From The Client: ' + message_back_decoded)

