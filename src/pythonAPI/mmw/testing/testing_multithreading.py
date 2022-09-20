"""
This is for testing
1) threading
2) locking (the add function) and making the method thread-safe

* results to print:
298 [(60, 'thread1', 9.8e-08), (70, 'thread2', 4.26e-07)]
299 [(60, 'thread1', 3.23e-07), (70, 'thread2', 7.64e-07)]
thread2 leads thread1: 0/300*  ---> 0 shows if locking works
 well.
"""


#import  Queue
from multiprocessing import Queue
from threading import Thread
from random import randrange
import time

class testclass(object):
   ret = "foo2"
   k = 0

   def foo(self, bar):
    print('hello {0}'.format(bar))
    return self.ret

   def add(self,i,j, name):
        # while self.lock != 0:
        #     time.sleep(0.02)
        # self.lock = 1
        random = randrange(1e3) / 1e9
        time.sleep(random)
        sum = i+j+self.k
        self.k += 10
        # self.lock = 0
        return sum, name, random

class testclass_locked(testclass):
   """Locked add method: here we introduced the lock variable and added a lcoking mechanism to add method."""
   lock = 0
   def add(self,i,j, name):
        while self.lock != 0:
            #pass
            time.sleep(8e-4)
        self.lock = 1
        random = randrange(1e3) / 1e9
        time.sleep(random)
        sum = i+j+self.k
        self.k += 10
        self.lock = 0
        return sum, name, random


def main():
    queues = list()
    threads_list = list()

    #c = testclass() # ["(60, 'thread1', 0.139)", "(70, 'thread2', 0.809)"] , here ther results 60 and 70 are mixed
    c = testclass_locked() # here always thread1 == 60 and thread2 == 70
    names = ["thread1","thread2"]
    results = {"thread1":0, "thread2":0}

    for i in range(0,2):
        name = names[i]
        #print("round: %d"%(i))
        que = Queue()
        queues.append(que)
        c.ret = "foo3"

        #t = Thread(target=lambda q, arg1: q.put(c.foo(arg1)), args=(que, 'world!'))
        c.k += 10
        t = Thread(target=lambda q, arg1, arg2, arg3: q.put(c.add(arg1, arg2, arg3)), args=(que, 23, 17, name))

        t.start()
        threads_list.append(t)

    # Join all the threads
    for t in threads_list:
        t.join()

    # Check thread's return value
    results = list()
    k = 0
    for que in queues:
        result = que.get()
        results.append(result)
        #print (result)
        k+=1
    #print(results)
    return results

if __name__ == "__main__":
    maxi = 300
    count = 0
    for i in range(0,maxi):
        results = main()
        #print(i)
        #if results[0] >= results[1]:
        print(i, results) # 29 ["(60, 'thread1', 0.162)", "(70, 'thread2', 0.461)"]
        if results[0][0] > results[1][0]: count +=1

    print("thread2 leads thread1: %d/%d"%(count, maxi))




