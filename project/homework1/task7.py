
def time_counter(f):
    def wrapper(*args):
        import time
        start_time = time.perf_counter()
        res = f(*args)
        print(int(time.perf_counter() - start_time))
        return res
    return wrapper


@time_counter
def func():
    import random
    import time
    time.sleep(random.randint(0, 10))


func()  # prints this execution time
func()  # prints this execution time
func()  # prints this execution time

