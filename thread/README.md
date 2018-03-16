# 多线程

Python是支持多线程的，主要通过***thread***和***threading***两个模块来实现的。
***thread***模块是比较底层的模块，而***threading***模块则是对thread进行了一些包装，更加方便使用。

# thread模块

#### 函数和常量
```python
import thread

thread.LockType             # 锁对象的一种，用于线程的同步
thread.error                # 线程的异常

thread.start_new_thread(function, args, kwargs)       # 创建一个新的线程
    # function: 线程执行函数
    # args:     线程执行函数的参数, 类似为tuple
    # kwargs:   是一个字典
    # 返回值:    返回线程的标识符
    
thread.exit()               # 线程退出函数
thread.allocate_lock()      # 生成一个未锁状态的锁对象
    # 返回值:    返回一个锁对象
```

锁对象的方法

```
lock.acquire([waitflag]) #获取锁
    * 无参数时, 无条件获取锁, 无法获取时, 会被阻塞, 知道可以锁被释放
    * 有参数时, waitflag = 0 时,表示只有在不需要等待的情况下才获取锁, 非零情况与上面相同
    * 返回值 :　获得锁成功返回True, 获得锁失败返回False

lock.release() #释放锁

lock.locked() #获取当前锁的状态
    * 返回值 : 如果锁已经被某个线程获取,返回True, 否则为False
```

#### 样例
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import thread
import time

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s : %s" % (thread_name, time.ctime(time.time()))

try:
    thread.start_new_thread(print_time, ("Thread-1", 2, ))
    thread.start_new_thread(print_time, ("Thread-2", 4, ))
except:
    print "Error: unable to start the thread"

while True:
    pass
```

# threading模块
>python的threading模块是对thread做了一些包装的，可以更加方便的被使用。
经常和Queue结合使用,Queue模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

#### 常用函数和对象
```python
import threading
#函数
threading.active_count()  #返回当前线程对象Thread的个数
threading.enumerate()  #返回当前运行的线程对象Thread(包括后台的)的list
threading.Condition()  #返回条件变量对象的工厂函数, 主要用户线程的并发
threading.current_thread()  #返回当前的线程对象Thread, 文档后面解释没看懂
threading.Lock()  #返回一个新的锁对象, 是在thread模块的基础上实现的 与acquire()和release()结合使用
 
#类
threading.Thread  #一个表示线程控制的类, 这个类常被继承
threading.Timer  #定时器,线程在一定时间后执行
threading.ThreadError  #引发中各种线程相关异常
```

###### Thread对象
>一般来说，使用线程有两种模式, 一种是创建线程要执行的函数, 把这个函数传递进Thread对象里，让它来执行. 
另一种是直接从Thread继承，创建一个新的class，把线程执行的代码放到这个新的class里。

常用两种方式运行线程（线程中包含name属性）：
* 在构造函数中传入用于线程运行的函数(这种方式更加灵活)
* 在子类中重写threading.Thread基类中run()方法（只重写__init__()和run()方法）

创建线程对象后, 通过调用start()函数运行线程, 然后会自动调用run()方法。
>通过设置｀daemon｀属性, 可以将线程设置为守护线程

```python
import threading
threading.Thread(group = None, target = None, name = None, args = (), kwars = {})
    # group :       应该为None
    # target :      可以传入一个函数用于run()方法调用,
    # name :        线程名 默认使用"Thread-N"
    # args :        元组, 表示传入target函数的参数
    # kwargs :      字典, 传入target函数中关键字参数
 
    # 属性:
    # name          #线程表示, 没有任何语义
    # doemon        #布尔值, 如果是守护线程为True, 不是为False, 主线程不是守护线程, 默认threading.Thread.damon = False
 
    # 类方法: 
    # run()         #用以表示线程活动的方法。
    # start()       #启动线程活动。
    # join([time])  #等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    # isAlive():    返回线程是否活动的。
    # getName():    返回线程名。
    # setName():    设置线程名。
```

###### 样例
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import threading
import time
 
def test_thread(count) :
    while count > 0 :
        print "count = %d" % count
        count = count - 1
        time.sleep(1)
 
def main() :
    my_thread = threading.Thread(target = test_thread, args = (10, ))
    my_thread.start()
    my_thread.join()
 
if __name__ == '__main__':
    main()
```

#### 常用多线程写法
1. 固定线程运行的函数
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import threading, thread
import time
 
 
class MyThread(threading.Thread):
    """docstring for MyThread"""
 
    def __init__(self, thread_id, name, counter) :
        super(MyThread, self).__init__()  #调用父类的构造函数 
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
 
    def run(self) :
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name
 
def print_time(thread_name, delay, counter) :
    while counter :
        time.sleep(delay)
        print "%s %s" % (thread_name, time.ctime(time.time()))
        counter -= 1
 
def main():
    #创建新的线程
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)
 
    #开启线程
    thread1.start()
    thread2.start()
 
 
    thread1.join()
    thread2.join()
    print "Exiting Main Thread"
 
if __name__ == '__main__':
    main()
```

2. 外部传入线程运行的函数
```python
#/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
 
class MyThread(threading.Thread):
    """
    属性:
    target: 传入外部函数, 用户线程调用
    args: 函数参数
    """
    def __init__(self, target, args):
        super(MyThread, self).__init__()  #调用父类的构造函数 
        self.target = target
        self.args = args
 
    def run(self) :
        self.target(self.args)
 
def print_time(counter) :
    while counter :
        print "counter = %d" % counter
        counter -= 1
        time.sleep(1)
 
def main() :
    my_thread = MyThread(print_time, 10)
    my_thread.start()
    my_thread.join()
 
if __name__ == '__main__':
    main()
```

#### 生产者消费者问题
>试着用python写了一个生产者消费者问题(伪生产者消费者), 
只是使用简单的锁, 感觉有点不太对, 下面另一个程序会写出正确的生产者消费者问题

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import thread, threading
import urllib2
import time, random
import Queue

share_queue = Queue.Queue()
my_lock = thread.allocate_lock()
class Producer(threading.Thread):
    def run(self):
        products = range(5)
        global share_queue
        while True:
            num = random.choice(products)
            my_lock.acquire()
            share_queue.put(num)
            print "Produce : ", num
            my_lock.release()
            time.sleep(random.random())

class Consumer(threading.Thread):
    def run(self):
        global share_queue
        while True:
            my_lock.acquire()
            if share_queue.empty():
                print "Queue is Empty..."
                my_lock.release()
                time.sleep(random.random())
                continue
            num = share_queue.get()
            print "Consumer : ", num
            my_lock.release()
            time.sleep(random.random())

def main():
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()

if __name__ == '__main__':
    main()
```