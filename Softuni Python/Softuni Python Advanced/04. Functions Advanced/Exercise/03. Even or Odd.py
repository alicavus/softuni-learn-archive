def even_odd(*args):
    result = []
    if args:
        result = [arg for arg in args[:-1] if arg % 2] if args[-1] == "odd" else [arg for arg in args[:-1] if not arg % 2]
    return result