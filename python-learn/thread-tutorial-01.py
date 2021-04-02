import time
import threading


def func(nnn):
    print('ran \n')
    time.sleep(1)
    print('done')


x = threading.Thread(target=func, args=(23,))
x.start()
print(threading.activeCount())
