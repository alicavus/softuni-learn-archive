class Calculator:
    @staticmethod
    def add(*args) -> int | float:
        if not args:
            raise ValueError("Empty list cannot be added")
        return sum(args)
    
    @staticmethod
    def subtract(*args) -> int | float:
        if not args:
            raise ValueError("Empty list cannot be subtracted")
        return Calculator.add(*[arg if idx == 0 else -arg for idx, arg in enumerate(args)])

    
    @staticmethod
    def multiply(*args) -> int | float:
        res = 1
        if not args:
            raise ValueError("Empty list cannot be multiplied")
        
        for arg in args:
            res = res * arg
        
        return res
    
    @staticmethod
    def divide(*args) -> float:
        if not args:
            raise ValueError("Empty list cannot be divided")
        
        return Calculator.multiply(*[arg if idx == 0 else 1 / arg for idx, arg in enumerate(args)])
    

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
print(Calculator.add(9, 8))