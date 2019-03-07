import socket


#  python server code
def main():
    # 创建socket套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器 绑定 本地端口
    tcp_socket.bind(("", 8888))
    # 监听某个端口
    tcp_socket.listen(8888)

    while True:
        # 接收数据 返回一个新的客户端socket
        client_socket, client_addr = tcp_socket.accept()
        recv_data = client_socket.recv(1024)
        client_socket.recvfrom(1024)

        print(client_addr)
        print(recv_data.decode("utf-8"))
        client_socket.close()
        pass
    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

# java client code
# public static void main(String[] args) {
#
#         try {
#             //1.创建客户端Socket，指定服务器地址和端口
#             Socket socket = new Socket("127.0.0.1", 8888);
#             //2.获取输出流，向服务器端发送信息
#             OutputStream os = socket.getOutputStream();//字节输出流
#             PrintWriter pw = new PrintWriter(os);//将输出流包装为打印流
#             pw.write("用户名：whf;密码：789");
#             pw.flush();
#             socket.shutdownOutput();//关闭输出流
#             //3.获取输入流，并读取服务器端的响应信息
#             InputStream is = socket.getInputStream();
#             BufferedReader br = new BufferedReader(new InputStreamReader(is));
#             String info = null;
#             while ((info = br.readLine()) != null) {
#                 System.out.println("我是客户端，服务器说：" + info);
#             }
#             //4.关闭资源
#             br.close();
#             is.close();
#             pw.close();
#             os.close();
#             socket.close();
#         } catch (UnknownHostException e) {
#             e.printStackTrace();
#         } catch (IOException e) {
#             e.printStackTrace();
#         }
#     }
