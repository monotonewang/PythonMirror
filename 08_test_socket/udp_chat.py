import socket


def send_msg(udp_socket):
    dest_ip = input("请输入目标ip:")
    dest_port = input("请输入对方的port:")
    send_data = str(input("请输入发送信息:"))
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def rece_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1025)
    recv_msg = recv_data[0]  # 数据信息
    recv_addr = recv_data[1]  # 地址信息
    # 打印信息
    print(recv_data)
    print("%s:%s" % (str(recv_addr), recv_msg))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 7788))
    while True:
        send_msg(udp_socket)


if __name__ == "__main__":
    main()
