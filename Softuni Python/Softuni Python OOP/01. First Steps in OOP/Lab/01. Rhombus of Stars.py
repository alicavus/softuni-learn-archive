class Rhombus:

    def __init__(self, n = 1):
        if not isinstance(n, int):
            raise TypeError(f"Invalid type: {type(n)}")
        
        elif n <= 0:
            raise ValueError(f"Invalid value: {n} is lower than 1")
        
        self.number = n
        
    def __repr__(self) -> str:
        res = [self.make_triangle()]
        if self.number > 1:
            res += [self.make_triangle(False)]
        return "\n".join(res)
    
    def make_line(self, line_number) -> str:
        return ' ' * (self.number - line_number) + " ".join(['*'] * line_number)
    
    def make_triangle(self, upper_part = True) -> str:
        if upper_part:
            start = 1
            end = self.number + 1
            step = 1
        else:
            start = self.number - 1
            end = 0
            step = -1
        
        return "\n".join([self.make_line(n) for n in range(start, end, step)])


def main():
    n = int(input())

    r = Rhombus(n)

    print(r)


if __name__ == "__main__":
    main()
        