#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Queue
import random
import thread
import threading
import time

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
