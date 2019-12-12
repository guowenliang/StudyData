'''Client端流程：
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
            '''
import socket

def clientFunc():

    addr = ("127.0.0.1",7852)

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "I WANNA YOU"

    #发送的数据必须是bytes格式

    data = text.encode()
#发送
    sock.sendto(data, addr)

    fdb,addr = sock.recvfrom(200)

    fdb = fdb.decode()

    print("反馈值：{0}".format(fdb))


if __name__ == '__main__':
    clientFunc()
    print("start")