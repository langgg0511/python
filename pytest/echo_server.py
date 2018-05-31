# import socket
# import time
# import threading
# #创建新线程
#
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
#         sock.close()
#         print('Connection from %s:%s close' % addr)
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 监听端口:
# s.bind(('127.0.0.1', 3000))
# s.listen(5)
# print('Waiting for connection...')
# while True:
#     # 接受一个新连接:
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接:
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 3000))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)

