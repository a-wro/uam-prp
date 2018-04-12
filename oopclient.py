#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

import tkinter as tk
from tkinter import simpledialog

username = 'test'
class Receiver(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        """Receive messages from server or other users"""
        while True:
            # append to GUI list box instead of printing it
            msg = self.socket.recv(1024).decode("utf8")
            print(msg)

class Sender(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        nameEntered = False
        """Send messages"""
        while True:
            if (nameEntered):
                print(username)
                msg = input(">")
                self.socket.send(bytes(msg, "utf8"))
            else:
                print(username)
                self.socket.send(bytes(username, "utf8"))
                nameEntered = True

def main():

    #socket and threads configuration
    host = 'localhost'
    port = 8888
    addr = (host, port)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(addr)

    sender_thread = Sender(client_socket) # create and run threads

    receiver_thread = Receiver(client_socket)
    receiver_thread.start()

    #GUI
    root = tk.Tk()
    namePrompt = tk.simpledialog.askstring('Test', 'Enter your name')
    username = namePrompt

    sender_thread.start() # start after name is received
    root.mainloop()
if __name__ == '__main__':
    main()
