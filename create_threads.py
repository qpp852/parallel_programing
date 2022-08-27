from threading import Thread
import time
from threading import Thread

def do_work():
    print("Starting work")
    # t = 1
    # for i in range(20000000):
    #     t += 1
    time.sleep(1)
    print("Finished work")

# multi threads (fake multi threads: it is quick because  thread release GIL when program sleep so that another thread could run.)
start = time.time()
for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
t.join()
print(time.time() - start)

# single threads
start = time.time()
for _ in range(5):
    do_work()
print(time.time() - start)