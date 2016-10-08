import time

class CountdownTask:
    def __init__(self):
        self._terminate = False
    def terminate(self):
        print("set termination")
        self._terminate = True
    def countdown(self, n):
        while n > 0:
            print("T-minus", n)
            n -= 1
            if (self._terminate):
                print("break loop")
                break
            time.sleep(5)


from threading import Thread
task = CountdownTask()
t = Thread(target=task.countdown, args=(10,))
t.setDaemon(True)  # So the thread will be terminated with main thread
t.start()
time.sleep(15)
task.terminate()
time.sleep(15)
