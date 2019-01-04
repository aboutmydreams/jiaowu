from collections import Counter
import threading,time,os,queue
 
class ThreadPool(object):
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self._q = queue.Queue(self.maxsize)
        for i in range(self.maxsize):
            self._q.put(threading.Thread)
 
    def getThread(self):
        return self._q.get()
 
    def addThread(self):
        self._q.put(threading.Thread)
 
def fun(num,p):
    print('this is thread [%s]'%num)
    time.sleep(1)
    p.addThread()
 
 
if __name__ == '__main__':
    pool = ThreadPool(2)
    for i in range(103):
        t = pool.getThread()
        a = t(target = fun,args = (i,pool))
        a.start()