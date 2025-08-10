def password_validator(password: str):
    is_valid = True

    #Length check
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    
    #Alnum check
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    
    #Digits check
    digits = [x for x in password if x.isdigit()]
    if len([x for x in password if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    
    if is_valid:
        print("Password is valid")

password_validator(input())