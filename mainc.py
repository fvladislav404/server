import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("7.tcp.eu.ngrok.io", 14900))
while 1:
    clientn = input("i")
    ans = clientn.encode()
    client.send(ans)
    