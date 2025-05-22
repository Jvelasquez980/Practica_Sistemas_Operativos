from threading import Semaphore as Semaphore

class GenProdCons:
    def __init__(self, size=10):
        self.size = size
        self.buffer = [None] * size
        self.mutex = Semaphore(1)
        self.full = Semaphore(0)
        self.empty = Semaphore(size)
        self.in_index = 0
        self.out_index = 0
        self.count = 0

    def put(self, item):
        self.empty.acquire()
        self.mutex.acquire()
        self.buffer[self.in_index] = item
        self.in_index = (self.in_index + 1) % self.size
        self.count += 1
        self.mutex.release()
        self.full.release()

    def get(self):
        self.full.acquire()
        self.mutex.acquire()
        item = self.buffer[self.out_index]
        self.out_index = (self.out_index + 1) % self.size
        self.count -= 1
        self.mutex.release()
        self.empty.release()
        return item

    def __len__(self):
        return self.count
