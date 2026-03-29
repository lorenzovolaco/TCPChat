import threading
import socket

host = '127.0.0.1' #host local, se não for na maquina você utiliza o ip address
port = 55555 #cuidado com o port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
server.bind((host, port))
server.listen()

clients = [] #lista de clientes
nicknames = [] #apelidos

def broadcast(message):
    for client in clients:
        client.send(message) #broadcast para todos clientes

def handle(client):
    while True:
        try:
            message = client.recv(1024) #bytes
            broadcast(message)
        except:
            index = clients.index(client)   #remover client se ele apresentar erros, ou sair
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat".encode('ascii'))
            clients.remove(nickname)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, adress = server.accept()
        print(f"Connected with {str(address)}") #mostra no console do server

        client.send("NICK".encode('ascii')) #demanda voc~e inserir o apelido
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}.")
        broadcast(f'{nickname} has joined the chat'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("Server started...")
receive()