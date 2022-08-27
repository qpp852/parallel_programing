import multiprocessing
import time

def do_work():
    print("starting work")
    i = 1
    for _ in range(20000000):
        i += 1
    print("finished work")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    start = time.time()
    for _ in range(5):
        p = multiprocessing.Process(target=do_work, args=())
        p.start()
    p.join()
    print(time.time() - start)

    start = time.time()
    for _ in range(5):
        do_work()
        # p = multiprocessing.Process(target=do_work, args=())
        # p.start()
    print(time.time() - start)