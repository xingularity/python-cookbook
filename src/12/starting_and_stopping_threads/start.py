import time

def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


from threading import Thread
t = Thread(target=countdown, args=(10,))
t.setDaemon(True)  # So the thread will be terminated with main thread
t.start()
time.sleep(50)
