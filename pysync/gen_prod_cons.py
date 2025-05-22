import threading
import logging

class GenProdCons:
    def __init__(self, size):
        assert size > 0, "Buffer size must be greater than 0"
        self.size = size
        self.buffer = [0] * size
        self.entry = 0
        self.outlet = 0
        self.quantity = 0

        self.mutex = threading.Semaphore(1)
        self.empty = threading.Semaphore(size)
        self.full = threading.Semaphore(0)

    def produce(self, item):
        self.empty.acquire()
        self.mutex.acquire()
        self.buffer[self.entry] = item
        self.entry = (self.entry + 1) % self.size
        self.quantity += 1
        logging.info("Produced item: %s", item)
        self.mutex.release()
        self.full.release()

    def consume(self):
        self.full.acquire()
        self.mutex.acquire()
        item = self.buffer[self.outlet]
        self.outlet = (self.outlet + 1) % self.size
        self.quantity -= 1
        self.mutex.release()
        self.empty.release()
        logging.info("Consumed item: %s", item)
        return item
