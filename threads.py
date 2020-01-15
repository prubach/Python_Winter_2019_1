import threading
import time

exit_flag = 0

class MyThread(threading.Thread):
    def __init__(self, threadId, name, delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.delay)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exit_flag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

thread1 = MyThread(1, "Thread 1", 1)
thread2 = MyThread(2, "Thread 2", 2)

thread1.start()
thread2.start()
# Wait for thread2 to exit
thread2.join()

print("Exiting Main Thread")