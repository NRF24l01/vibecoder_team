from time import time

class Timer():
    def __init__(self):
        self.timer = time()
    
    def stop(self) -> float:
        return time()-self.timer