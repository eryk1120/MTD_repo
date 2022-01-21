import time

def timeIt(func):
    def wrapper(*arg,**kwargs):
        t = time.time()
        res = func(*arg)
        print(f"Function '{func.__name__}' took {(time.time() - t):.10f}  seconds to run")
        return res

    return wrapper
