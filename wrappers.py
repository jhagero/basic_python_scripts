def my_decorator(func):
    def wrapper():
        print(f"Trying {func.__name__}")
        try:
            func()
            print("Complete")
        except Exception as e:
            print(f"{func.__name__} failed! {e}")
    return wrapper

@my_decorator
def do_this():
    print("Doing this!")

@my_decorator
def do_that():
    print("Doing that!")

@my_decorator
def risky():
    x = 1 / 0

do_that()
do_this()
risky()
