import threading

sum = 0
loopSum = 1000000
lock = threading.Lock()


def MyAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        #上锁，申请锁
        lock.acquire()
        sum+=1
        #释放锁
        lock.release()
def MyMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        #上锁，申请锁
        lock.acquire()
        sum-=1
        #释放锁
        lock.release()
if __name__ == '__main__':
    print("Starting*******{0}".format(sum))

    t1 = threading.Thread(target=MyAdd, args=())
    t1.start()
    t2 = threading.Thread(target=MyMinu, args=())
    t2.start()
    t1.join()
    t2.join()
    print("Done...{0}".format(sum))
    '''MyAdd()
    print(sum)
    MyMinu()
    print(sum)'''
