from time import time

class Timer:
   
   def __init__(self):
       self.start_time = None
       self.end_time = None
       
   def __enter__(self):
       self.start_time = time()
       return self
       
   def __exit__(self, exc_type, exc_val, exc_tb):
       self.end_time = time()
