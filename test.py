import threading
import time



def writer():
    for i in range(10):
        print(i)


def writer1():
    for id in range(10):
        print("f")

t1 = threading.Thread(target=writer)
t2 = threading.Thread(target=writer1)

t1.start()
t2.start()
