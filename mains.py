import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",1024))

server.setblocking(False)
server.listen(5)
clients = []
def acc():
    while 1:
        try:
            for client in clients:
                sms = client.recv(1024).decode()
                print(sms)
        except:
            pass
threading.Thread(target=acc).start()
while 1:
    try:
        info, ip = server.accept()
        print(f"подключение  {ip}")
        clients.append(info)
    except:
        pass