'''
利用time函数，生成两个函数
顺序调用计算总运行时间
'''
import time
import threading
def loop1():
    #ctime 得到当前时间
    print("Start loop 1 at:",time.ctime())
    #睡眠多长时间，单位是秒
    time.sleep(6)
    print("End loop 1 at:", time.ctime())

def loop2():
    #ctime 得到当前时间
    print("Start loop 2 at:",time.ctime())
    #睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def loop3():
    #ctime 得到当前时间
    print("Start loop 3 at:",time.ctime())
    #睡眠多长时间，单位是秒
    time.sleep(8)
    print("End loop 3 at:", time.ctime())

def main():
    print("Starting at:",time.ctime())
    #生成一个线程实例
    t1 = threading.Thread(target=loop1,args=())
    t1.setName("Thr_1")
    t1.start()
    t2 = threading.Thread(target=loop2,args=())
    t2.setName("Thr_2")
    t2.start()
    t3 = threading.Thread(target=loop3,args=())
    t3.setName("Thr_3")
    t3.start()
    #预计三秒后，线程2结束
    time.sleep(3)

    #enumerate得到正在运行的子线程，线程1  3
    for thr in threading.enumerate():
        print("the running thread's name are :{0}".format(thr.getName()))
    print("the count of the running threads:{}".format(threading.active_count()))
    print("All done at:",time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
