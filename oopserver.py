#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class ChatServer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.socket = socket
        self.server = socket(AF_INET, SOCK_STREAM)
        self.clients = {} # keep track of clients

        host = '127.0.0.1'
        port = 8888
        addr = (host, port)

        self.server.bind(addr)
        self.server.listen(3)
        """Sets up handling for incoming clients."""
        while True:
            c, addr = self.server.accept() # connection(socket), address
            print("{} has connected.".format(addr))
            c.send(bytes("Enter your name", "utf8"))

            clientThread = Thread(target=self.clientHandler, args=(c,))
            clientThread.start()

    def clientHandler(self, client):  # Takes client socket as argument
        # When new client joins
        name = client.recv(1024).decode("utf8")
        client.send(bytes('User connected: {}'.format(name), "utf8")) # welcome message
        msg = "{} has joined the chat".format(name)
        self.broadcast(bytes(msg, "utf8"))
        self.clients[client] = name # map socket to client's name
        # lets client chat
        while True:
            msg = client.recv(1024)
            if (msg.decode("utf8") != '!quit'):
                sender = name + ':'
                self.broadcast(msg, sender)
            else:
                client.close()
                del self.clients[client]
                print("{} has left the chat.".format(name))
                self.broadcast(bytes("{} has left the chat.".format(name), "utf8"))
                break

    def broadcast(self, msg, name=""):  # msg is bytes
        """Display message to all clients"""
        for sock in self.clients:
            sock.send(bytes(name, 'utf8') + msg)

def main():
    chatServer = ChatServer()
    print("Running..")
    chatServer.start()
    chatServer.join()

if __name__ == "__main__":
    main()
