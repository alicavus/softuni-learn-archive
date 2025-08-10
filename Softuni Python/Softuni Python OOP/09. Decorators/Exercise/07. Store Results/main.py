from pathlib import Path as p

class store_results:
    def __init__(self, func):
        self.func = func
        self.log_file = p(__file__).with_name("results").with_suffix(".txt")
    
    def __call__(self, *args, **kwds):

        result = self.func(*args, **kwds)

        try:
            with self.log_file.open("a") as log_file:
                log_file.write(f"Function '{self.func.__name__}{args}' was called. Result: {result}\n")
        except Exception as e:
            print(e.args)
        
        return result


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)