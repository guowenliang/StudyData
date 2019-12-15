import socket

def tcp_srv():
    #1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后新建立的socket
    # 需要用到两个参数
    # AF_INET:含义同 UPD
    # SOCK_STREAM:表明使用的是tcp进行通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.  绑定端口和地址
    # 此地址信息是一个元组类型内容，元组分两部分，第一部分为字符串，代表ip，第二部分为端口号
    addr = ("127.0.0.1",8989)
    sock.bind(addr)
    # 3. 监听接入的访问socket
    sock.listen()
    while True:
        #4. 接受访问的socket，可以理解为接受访问即建立了一个通讯的链接通道
        #accept 返回的元组第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()
        # 5. 接受对方的发送内容，利用接收到的socket接收内容
        # 500 代表接收使用的sizebuffer
        msg = skt.recv(500)
        # 接收得到的是bytes格式
        # 得到str格式需要解码
        msg = msg.decode()

        rst = "Received msg: {0} from {1}".format(msg,addr)
        print(rst)
        #6. 如果有必要，给对方发送反馈信息
        skt.send(rst.encode())
        #7. 关闭链接通路
        skt.close()

if __name__ == '__main__':
    print("Starting tcp server....")
    tcp_srv()
    print("Ended tcp server....")