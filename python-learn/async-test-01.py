import time
import asyncio


@asyncio.coroutine
def periodic(period):
    def g_tick():
        t = time.time()
        count = 0
        while True:
            count += 1
            yield max(t + count * period - time.time(), 0)
    g = g_tick()

    while True:
        print('periodic', time.time())
        yield from asyncio.sleep(next(g))


loopy = asyncio.get_event_loop()
task = loopy.create_task(periodic(1))
loopy.call_later(5, task.cancel)

try:
    loopy.run_until_complete(task)
except asyncio.CancelledError:
    pass
