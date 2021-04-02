import threading
import time

global nn
nn = 1


def pippo():
    print("pippo " + str(nn))


def startTask():
    nn = 2
    t = MyThread(0.1)
    t.start()
    time.sleep(3)
    t.join(1)  # wait 1s max


class MyThread(threading.Thread):

    def __init__(self, sleep_time=0.1):

        self._stop_event = threading.Event()
        self._sleep_time = sleep_time
        """call base class constructor"""
        super().__init__()

    def run(self):
        """main control loop"""
        while not self._stop_event.isSet():
            # do work
            # print("hi " + str(nn))
            pippo()
            self._stop_event.wait(self._sleep_time)

    def join(self, timeout=None):
        """set stop event and join within a given time period"""
        self._stop_event.set()
        super().join(timeout)
        # nn = 2
        startTask()


# if __name__ == "__main__":
#     t = MyThread(0.1)
#     t.start()
#     time.sleep(3)
#     t.join(1)  # wait 1s max
startTask()
