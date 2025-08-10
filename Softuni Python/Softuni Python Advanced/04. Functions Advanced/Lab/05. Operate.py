def operate(operator, *args):
    def addition(left, right):
        return left + right
    
    def substracrion(left, right):
        return left - right
    
    def multiplication(left, right):
        return left * right
    
    def division(left, right):
        return left / right
    
    result = args[0]
    for arg in args[1:]:
        match operator:
            case "+":
                result = addition(result, arg)
            case "-":
                result = substracrion(result, arg)
            case "*":
                result = multiplication(result, arg)
            case "/":
                result = division(result, arg)
    return result