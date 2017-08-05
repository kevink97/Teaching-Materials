#!/usr/bin/python3
import socket, sys, threading

# Simple chat client that allows multiple connections via threads

PORT = 3333 # the port number to run our server on

__version__ = "0.0.1"

class ChatServer(threading.Thread):
    conns = list()

    def __init__(self, port, host='localhost'):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {} # current connections
        try:
            self.server.bind((self.host, self.port))
        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()

        self.server.listen(10)

    # Not currently used. Ensure sockets are closed on disconnect
    def exit(self):
        self.server.close()

    def run_thread(self, conn, addr):
        ChatServer.conns.append(conn)
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        while True:
            try:
                data = conn.recv(1024)
                if len(data) == 0:
                    break
                reply = data
                print(str(reply, 'utf-8'))
                for minicon in ChatServer.conns:
                    # send instead of sendall to prevent overhead
                    minicon.sendall(reply)
            except KeyboardInterrupt:
                break
        conn.close() # Close
        ChatServer.conns.remove(conn)

    def run(self):
        print('Waiting for connections on port %s\nPress ctrl + c to destroy server' % (self.port))
        # We need to run a loop and create a new thread for each connection
        while True:
            conn = None
            addr = None
            try:
                conn, addr = self.server.accept()
                if not conn:
                    continue;
            except KeyboardInterrupt:
                if conn:
                    exit()
                print('\nServer has been killed')
                break
            threading.Thread(target=self.run_thread, args=(conn, addr)).start()

if __name__ == '__main__':
    server = ChatServer(PORT)
    server.run()
