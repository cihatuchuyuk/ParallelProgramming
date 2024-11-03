import time
import sys

custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
   """
   Calculates (x^a + y^b) / c

   :param x: First base (positional-only)
   :type x: int
   :param y: Second base (positional-only)
   :type y: int
   :param a: First exponent (positional-or-keyword) 
   :type a: int
   :param b: Second exponent (positional-or-keyword)
   :type b: int
   :param c: Divisor (keyword-only)
   :type c: int
   :return: Result of calculation
   :rtype: float
   """
   return (x**a + y**b) / c

def fn_w_counter() -> tuple[int, dict[str, int]]:
   """
   Tracks function calls and their sources

   :return: Total calls and call counts by source
   :rtype: tuple[int, dict[str, int]]
   """
   if not hasattr(fn_w_counter, "calls"):
       fn_w_counter.calls = 0
       fn_w_counter.sources = {}
   
   fn_w_counter.calls += 1
   fn_w_counter.sources[__name__] = fn_w_counter.sources.get(__name__, 0) + 1
   
   return fn_w_counter.calls, fn_w_counter.sources

def performance(func):
   """
   Measures function performance metrics

   :param func: Function to measure
   :return: Wrapper with statistics
   """
   if not hasattr(performance, 'count'):
       performance.count = 0
       performance.exec_time = 0
       performance.mem_used = 0

   def wrapper(*args, **kwargs):
       performance.count += 1
       
       start_time = time.time()
       result = func(*args, **kwargs)
       performance.exec_time += time.time() - start_time
       
       performance.mem_used += sys.getsizeof(result)
       return result

   return wrapper
