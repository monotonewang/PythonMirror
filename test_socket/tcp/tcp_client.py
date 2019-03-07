import socket


def main():
    # 创建socket套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    dest_ip = input("请输入目标ip:")
    dest_port = input("请输入对方的port:")
    server_addr = (dest_ip, dest_port)
    tcp_socket.connect(server_addr)

    send_data = str(input("请输入发送信息:"))
    tcp_socket.send(send_data.encode("utf-8"))
    # 关闭套接字
    tcp_socket.close()

    pass


if __name__ == '__main__':
    main()
