# 多线程
http://python.jobbole.com/88411/

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
thread_sample.py

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
threading_sample.py

#### 常用多线程写法
1. 固定线程运行的函数
fixed_thread.py

2. 外部传入线程运行的函数
outside_function_thread.py

#### 生产者消费者问题
>试着用python写了一个生产者消费者问题(伪生产者消费者), 
只是使用简单的锁, 感觉有点不太对, 下面另一个程序会写出正确的生产者消费者问题

producer_consumer_1.py

杀死多线程程序方法: 使用control + z挂起程序(程序依然在后台, 可以使用ps aux查看), 
使用了wait()和notify()来解决上述问题

>当然最简答的方法是直接使用Queue，Queue封装了Condition的行为, 
如wait(), notify(), acquire(), 没看文档就这样, 使用了Queue竟然不知道封装了这些函数

producer_consumer_2.py

#### 简单锁

>如果只是简单的加锁解锁可以直接使用threading.Lock()生成锁对象, 然后使用acquire()和release()方法
样例
simple_lock.py

#### Condition
>如果是向生产者消费者类似的情形, 使用Condition类 或者直接使用Queue模块

条件变量中有acquire()和release方法用来调用锁的方法, 有wait(), notify(), notifyAll()方法, 后面是三个方法必须在获取锁的情况下调用, 否则产生RuntimeError错误.
* 当一个线程获得锁后, 发现没有期望的资源或者状态, 就会调用wait()阻塞, 并释放已经获得锁, 知道期望的资源或者状态发生改变
* 当一个线程获得锁, 改变了资源或者状态, 就会调用notify()和notifyAll()去通知其他线程

```python
#官方文档中提供的生产者消费者模型
# Consume one item
cv.acquire()
while not an_item_is_available():
    cv.wait()
get_an_available_item()
cv.release()
 
# Produce one item
cv.acquire()
make_an_item_available()
cv.notify()
cv.release()
```

```python
#threading.Condition类
thread.Condition([lock])
可选参数lock: 必须是Lock或者RLock对象, 并被作为underlying锁(悲观锁?), 否则, 会创建一个新的RLock对象作为underlying锁
 
类方法:
acquire()  #获得锁
release()  #释放锁
wait([timeout])  #持续等待直到被notify()或者notifyAll()通知或者超时(必须先获得锁),
#wait()所做操作, 先释放获得的锁, 然后阻塞, 知道被notify或者notifyAll唤醒或者超时, 一旦被唤醒或者超时, 会重新获取锁(应该说抢锁), 然后返回
notify()  #唤醒一个wait()阻塞的线程.
notify_all()或者notifyAll()  #唤醒所有阻塞的线程
```