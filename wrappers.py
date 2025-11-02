import time
from datetime import datetime, timezone

def smart_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs) # <- Any args
            elapsed = (time.time() - start)*1000
            print(f"{func.__name__}() completed in {elapsed:.3f}ms")
            return result
        except Exception as e:
            elapsed = (time.time() - start)*1000
            print(f"{func.__name__} failed: {e}")
            raise # prevent misleading tracebacks by passing  failed function returns
    return wrapper

@smart_wrapper
def do_this():
    print("Doing this!")

@smart_wrapper
def do_that():
    print("Doing that!")

@smart_wrapper
def risky():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print("Can't divide by zero, homey. Have a nice shiny 0 instead.")        
        return 0

@smart_wrapper
def slow_sleep(n):
    time.sleep(n)

@smart_wrapper
def fast_math(x, y):
    return x ** y

@smart_wrapper
def load_level():
    # heavy YAML + GLTF
    ...
    
@smart_wrapper
def update_physics():
    # collision checks
    ...


do_that()
do_this()
risky()
slow_sleep(1)       # -> slow_sleep(): ~1000ms
fast_math(2, 10)    # -> fast_math(): 0
