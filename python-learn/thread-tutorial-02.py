import time
import threading

ls = []


def count(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.25)


def count2(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.25)


x = threading.Thread(target=count, args=(5,))
x.start()

x.join()

y = threading.Thread(target=count2, args=(5,))
y.start()

y.join()

print(ls)
# print("done \n")
# print(threading.activeCount())
