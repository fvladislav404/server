import socket
servak = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 1024))

servak.setblocking(False)
servak.listen(1)
print("Сервер очікує підключення")
clients = []
while True:
    try:
        info, ip_adress = servak.accept()
        print(f"До мене під'єднався кліент с ip{ip_adress}")
        info.setblocking(False)
        clients.append(info)
    except:
        pass
for client in clients:
    try:
        client.send("не удалось подключиться".encode())    
    except:
        print("подключение")
        clients.remove(client)
    
data = info.recv(1024).decode()


info.send(f"Привіт {data}".encode())

info.close()
servak.close()import socket
servak = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 1024))

servak.setblocking(False)
servak.listen(1)
print("Сервер очікує підключення")
clients = []
while True:
    try:
        info, ip_adress = servak.accept()
        print(f"До мене під'єднався кліент с ip{ip_adress}")
        info.setblocking(False)
        clients.append(info)
    except:
        pass
for client in clients:
    try:
        client.send("не удалось подключиться".encode())    
    except:
        print("подключение")
        clients.remove(client)
    
data = info.recv(1024).decode()


info.send(f"Привіт {data}".encode())

info.close()
servak.close()import socket
servak = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 1024))

servak.setblocking(False)
servak.listen(1)
print("Сервер очікує підключення")
clients = []
while True:
    try:
        info, ip_adress = servak.accept()
        print(f"До мене під'єднався кліент с ip{ip_adress}")
        info.setblocking(False)
        clients.append(info)
    except:
        pass
for client in clients:
    try:
        client.send("не удалось подключиться".encode())    
    except:
        print("подключение")
        clients.remove(client)
    
data = info.recv(1024).decode()


info.send(f"Привіт {data}".encode())

info.close()
servak.close()import socket
servak = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 1024))

servak.setblocking(False)
servak.listen(1)
print("Сервер очікує підключення")
clients = []
while True:
    try:
        info, ip_adress = servak.accept()
        print(f"До мене під'єднався кліент с ip{ip_adress}")
        info.setblocking(False)
        clients.append(info)
    except:
        pass
for client in clients:
    try:
        client.send("не удалось подключиться".encode())    
    except:
        print("подключение")
        clients.remove(client)
    
data = info.recv(1024).decode()


info.send(f"Привіт {data}".encode())

info.close()
servak.close()

data = info.recv(1024).decode()
print(data)

info.send(f"Привіт {data}".encode())

info.close()
servak.close()import socket
servak= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 4444))

servak.listen(1)
print("Сервер очікує підключення")

info, ip_adress = servak.accept()
print(f"До мене під'єднався кліент с ip{ip_adress}")

data = info.recv(1024).decode()
print(data)

info.send(f"Привіт {data}".encode())

info.close()
servak.close()

