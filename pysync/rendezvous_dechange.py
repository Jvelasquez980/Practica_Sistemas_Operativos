import threading

class RendezvousDEchange:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.has_first = False
        self.first_value = None

    def echanger(self, value):
        with self.condition:
            if not self.has_first:
                # Primer hilo llega
                self.first_value = value
                self.has_first = True
                self.condition.wait()
                result = self.second_value
                self.has_first = False
                return result
            else:
                # Segundo hilo llega
                self.second_value = value
                self.condition.notify()
                return self.first_value