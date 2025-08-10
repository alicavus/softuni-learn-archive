def formatter(char):
    def decorator(func):
        def wrapper(*args):
            return f"<{char}>{func(*args)}</{char}>"
        return wrapper
    return decorator

make_bold = formatter('b')
make_italic = formatter('i')
make_underline = formatter('u')

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
