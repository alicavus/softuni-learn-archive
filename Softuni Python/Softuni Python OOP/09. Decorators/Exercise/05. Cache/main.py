class cache_class:
    def __init__(self, func):
        self.func = func
        self.log = {}
    
    def __call__(self, arg):
        if arg in self.log:
            return self.log[arg]
        res = self.func(arg)
        self.log[arg] = res
        return res

def cache(func):
    log = {}
    def wrapper(n):
        if n in log:
            return log[n]
        log[n] = func(n)
        return log[n]
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(0)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)