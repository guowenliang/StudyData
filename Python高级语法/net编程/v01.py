'''Server端流程：
1.
建立socket，socket是负责具体通信的实例
2.
绑定，为创建的socket指派固定的端口和ip
3.
接受对方发送的内容
4.
给对方发送反馈，此步骤为非必需步骤
'''
#socket模块负责socket编程
import socket

# 模拟服务器的函数
def serverFunc():
    #1. 建立socket
    # socket.AF_INET:使用ipv4协议族
    # socket.SOCK_DGRAM：使用UPD通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2. 绑定IP地址和port
    #127.0.0.1：这个ip地址代表机器本身
    # 7852:随便指定的端口号
    #地址是一个tuple类型，（ip,port）
    addr = ("127.0.0.1",7852)
    sock.bind(addr)

    #接收对方消息
    #等待方式为死等，没有其他可能
    # recvfrom接受的返回值是一个元组，前一项表示数据，后一项表示地址
    # 参数含义是缓冲区大小
    data,addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    # 发送过来得到数据是bytes格式，必须通过解码方式才能得到str格式内容
    #decode默认参数㐊utf-8
    text = data.decode()
    print(text)
    print(type(text))
    print("服务器接收:{}".format(text))
    #给对方返回的消息
    rsp = " I AM NOT HUNGRY"
    #发送的数据需要编码
    #默认utf-8
    data = rsp.encode()

    sock.sendto(data,addr)


if __name__ == '__main__':
    print("starting server..")
    serverFunc()
    print("ending*****")


