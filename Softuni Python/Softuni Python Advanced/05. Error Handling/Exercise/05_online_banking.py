# Exercise: Error Handling
# 5. Online Banking

# Exceptions
class MoneyNotEnoughError(Exception):
    '''Raised when balance is not sufficient'''
    pass

class PINCodeError(Exception):
    '''Raised when wrong PIN code is provided'''
    pass

class UnderageTransactionError(Exception):
    '''Raised when sender is not reached adulthood'''
    pass

class MoneyIsNegativeError(Exception):
    '''Raised when money amount is bellow 0'''
    pass


# Definitions
INITIAL_FIELD_SEPARATOR = ", "
TRANSACTION_FIELD_SEPARATOR = "#"
END_COMMAND = "End"
LEGAL_AGE = 18

SALARY_INVESTMENT_PERCENT = 50

pin, balance, age = input().split(INITIAL_FIELD_SEPARATOR)
balance = float(balance)
age = int(age)

while True:
    commands = input().split(TRANSACTION_FIELD_SEPARATOR)
    command = commands[0]

    if command == END_COMMAND:
        break

    elif command == "Send Money":
        money, pin_code = float(commands[1]), commands[2]

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        
        if pin_code != pin:
            raise PINCodeError("Invalid PIN code")
        
        if age < LEGAL_AGE:
            raise UnderageTransactionError(f"You must be {LEGAL_AGE} years or older to perform online transactions")
        
        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")
    
    elif command == "Receive Money":
        money = float(commands[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        
        amount_to_deposit = money * (1 - SALARY_INVESTMENT_PERCENT * 0.01)
        
        balance += amount_to_deposit

        print(f"{amount_to_deposit:.2f} money went straight into the bank account")
        

        



