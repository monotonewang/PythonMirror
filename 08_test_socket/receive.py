import socket

# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定一个本地信息
localaddr = ("192.168.1.1", 7788)
udp_socket.bind(localaddr)
# 接收数据
recv_data = udp_socket.recvfrom(1025)
recv_msg = recv_data[0]  # 数据信息
recv_addr = recv_data[1]  # 地址信息
# 打印信息
print(recv_data)
print("%s:%s" % (str(recv_addr), recv_msg))
# 关闭套接字
udp_socket.close()
