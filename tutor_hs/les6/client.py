# ifconfig |grep inet to get the ip address for LAN connection
import socket, sys, threading
PORT = 3333
class ChatClient(object):
    users = list()

    def __init__(self, username, port, host='localhost'):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, port))
        self.username = username
        ChatClient.users.append(username)

    def send_message(self, msg):
        self.socket.sendall(str.encode("[" + self.username + "]: " + msg))

    def listen(self, startmsg='>'):
        msg = str(self.socket.recv(1024), 'utf-8')
        if len(msg) > 0:
            return msg + "\n" + startmsg

def always_listen():
    listener = ChatClient('listener', PORT)
    while (True):
        try:
            listener.listen()
        except KeyboardInterrupt:
            break
    listener.socket.close()

if __name__ == '__main__':
    threading.Thread(target=always_listen).start()
    client = ChatClient('kevink97', PORT)
    while (True):
        try:
            msg = input("Type your message: ")
            client.send_message(msg)
        except KeyboardInterrupt:
            break
    client.socket.close()
