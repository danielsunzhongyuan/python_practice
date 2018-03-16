# 多线程

Python是支持多线程的，主要通过***thread***和***threading***两个模块来实现的。
***thread***模块是比较底层的模块，而***threading***模块则是对thread进行了一些包装，更加方便使用。

# thread模块

#### 函数和常量
```
import thread

thread.LockType             # 锁对象的一种，用于线程的同步
thread.error                # 线程的异常

thread.start_new_thread(function, args[, kwargs])       # 创建一个新的线程
    * function: 线程执行函数
    * args:     线程执行函数的参数, 类似为tuple
    * kwargs:   是一个字典
    * 返回值:    返回线程的标识符
    
thread.exit()               # 线程退出函数
thread.allocate_lock()      # 生成一个未锁状态的锁对象
    * 返回值:    返回一个锁对象
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