def multiply(times):

    def decorator(function):
        def wrapper(params):
            return times * function(params)
        return wrapper

    return decorator


class A:
    @property
    def a(self):
        pass
    
    @a.getter
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        self.__a = value

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
