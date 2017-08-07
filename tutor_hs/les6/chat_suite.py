from server import ChatServer
from client import ChatClient
import threading
import os

HOST = 'attu1.cs.washington.edu' # 'localhost' works
PORT = 3333

prev = ''

def run_server(port=PORT):
    server = ChatServer(PORT, '0.0.0.0')
    server.run()

def get_prev_msg():
    global prev
    return prev[prev.find(':') + 2:prev.rfind('\n')]

# helper method for listening
def always_listen(username, port=PORT):
    # attu server conf
    listener = ChatClient('listener', port, HOST)
    while (True):
        try:
            res = listener.listen()
            global prev
            if res == prev:
                prev = ''
            if not res == '' and not res == prev:
                prev = res
            if not (res[res.find('[') + 1: res.find(']')] == username):
                print(res, end='')
        except KeyboardInterrupt:
            break
    listener.socket.close()

def start_client(username, port=PORT):
    threading.Thread(target=always_listen, args=[username]).start()
    print(HOST)
    client = ChatClient(username, port, HOST)
    return client

def send_message(client, msg):
    client.send_message(msg)

def end_client(client):
    client.socket.close()
