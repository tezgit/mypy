import threading
import time

counter = 1


def tezCallBack(iTimeSec, isRepeated):
    global counter
    counter += 1
    print("-- doing my stuf --!  >> " + str(counter))

    if (isRepeated == True and counter < 10):
        threading.Timer(iTimeSec, tezCallBack, [
            iTimeSec, isRepeated]).start()
    else:
        print(" I am done doing my stuf!")


def startTezTimer(iTimeSec, isRepeated):
    threading.Timer(iTimeSec, tezCallBack, [iTimeSec, isRepeated]).start()


def main():
    startTezTimer(0.25, True)  # start timer and callback

    while True:
        # print(">> loop <<")
        # time.sleep(1)
        pass


if __name__ == '__main__':
    main()
