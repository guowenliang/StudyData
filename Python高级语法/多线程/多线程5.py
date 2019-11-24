'''
利用time函数，生成两个函数
顺序调用计算总运行时间
'''
import time
import threading
def loop1(in1):
    #ctime 得到当前时间
    print("Start loop 1 at:",time.ctime())
    print("参数",in1)
    #睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2(in1,in2):
    #ctime 得到当前时间
    print("Start loop 2 at:",time.ctime())
    print("参数", in1,"和参数",in2)
    #睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def main():
    print("Starting at:",time.ctime())
    #启动多线程的意思是用多个线程去执行某个函数
    #启动多线程函数为start_new_thread
    #参数两个，一个是需要运行的函数名，第二是函数的参数作为元组使用，为空则使用空元组
    #注意，如果函数只有一个参数，需要参数后有一个逗号
    t1 = threading.Thread(target=loop1,args=("呵呵445",))
    t1.start()
    t2 = threading.Thread(target=loop2,args=("hh","hhhhh"),)
    t2.start()
    t1.join()
    t2.join()
    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()

