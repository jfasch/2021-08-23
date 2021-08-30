import threading
import time


class EinThread(threading.Thread):
    def __init__(self, message, interval):
        super().__init__()
        self.message = message
        self.interval = interval

    def run(self):
        while True:
            print(self.message)
            time.sleep(self.interval)

t1 = EinThread('seas', 1.2)
t2 = EinThread('hi', 3.1)

t1.start()
t2.start()
