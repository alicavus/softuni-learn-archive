# Exercise: Error Handling
# 3. Password Validator

# Exceptions
class PasswordTooShortError(Exception):
    '''Raised when password does not meet minimal length requirement'''
    pass

class PasswordTooCommonError(Exception):
    '''Raised when password is not mixture of digits, letters, and allowed special characters'''
    pass

class PasswordNoSpecialCharactersError(Exception):
    '''Raised when password does not contain any allowed special symbol'''
    pass

class PasswordContainsSpacesError(Exception):
    '''Raised when whitespace is present in password''' # whitespace or horizontal space only?
    pass

# Definitions
PASSWORD_MIN_LENGTH = 8
SPECIAL_CHARACTERS = ["@", "*", "&", "%"]
END_COMMAND = "Done"

while True:
    password = input()

    if password == END_COMMAND:
        break

    if len(password) < PASSWORD_MIN_LENGTH:
        raise PasswordTooShortError(f"Password must contain at least {PASSWORD_MIN_LENGTH} characters")
    
    if password.isdigit() or password.isalpha() or all(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    
    if all(ch not in SPECIAL_CHARACTERS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    
    if any(ch.isspace() for ch in password):
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    
    print("Password is valid")

