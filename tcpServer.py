#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
from socketserver import TCPServer,BaseRequestHandler

class handlerTcpData(BaseRequestHandler):
    def handle(self):
        print('Server start...')
        conn = self.request
        print('Get connect:', self.client_address)
        while True:
            client_data = conn.recv(2048)
            if client_data == "quit":
                print('receive quit command, quit!')
                break
            else:
                print('receive data:%s' % client_data.decode('utf-8'))
                print('start send...')
                conn.sendall(client_data)

if __name__ == '__main__':
    server = TCPServer(('127.0.0.1', 8800), handlerTcpData)
    server.serve_forever()
'''
import socket,threading,time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8800))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
