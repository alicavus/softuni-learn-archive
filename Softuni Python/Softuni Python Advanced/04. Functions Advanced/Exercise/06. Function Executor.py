def func_executor(*args):
    return "\n".join([f"{arg[0].__name__} - {arg[0](*arg[1])}" for arg in args])