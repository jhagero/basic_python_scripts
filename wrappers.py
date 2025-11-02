import time
from datetime import datetime, timezone

def smart_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            start = time.time()
            # -> Convert to readable timestamp
            timestamp = datetime.fromtimestamp(start, tz=timezone.utc)
            print(f"Trying {func.__name__}() @[{timestamp.strftime('%H:%M:%S.%f')[:-3]}s]")

            result = func(*args, **kwargs) # <- Any args
            elapsed = (time.time() - start)*1000

            print(f"Completed {func.__name__}() in {elapsed:.3f}ms")
            return result
        except Exception as e:
            print(f"{func.__name__} failed! {e}")
    return wrapper

@smart_wrapper
def do_this():
    print("Doing this!")

@smart_wrapper
def do_that():
    print("Doing that!")

@smart_wrapper
def risky():
    x = 1 / 0

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
