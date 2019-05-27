import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建一个udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '192.168.10.29'

# 可以使用套接字收发数据
s.sendto(b"this is udp server", (ip, 3020))

# 关闭套接字
s.close()
