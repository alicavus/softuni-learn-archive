# Exercise: Error Handling
# 2. Email Validator

# Exceptions
class NameTooShortError(Exception):
    '''Raised when required minimal `name` length is not satisfied'''
    pass

class MustContainAtSymbolError(Exception):
    '''Raised when `@` symbol is not present in the e-mail address'''
    pass

class InvalidDomainError(Exception):
    '''Raised when TLD part is not whitelisted''' #Maybe use more neutral language?
    pass

# Definitions
USERNAME_MIN_LENGTH = 5
ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]
END_COMMAND = "End"


# This solution is **NOT** a proper way to parse valid e-mail address.
# Just training custom exceptions.
# In real situations use **RegEx** and custom classes.

while True:
    email = input()

    if email == END_COMMAND:
        break
    
    if "@" not in email:
        # This solution does not handles issues with more than one `@` symbol
        # i.e. `myuser@myprovider@mydomain.net`
        raise MustContainAtSymbolError("Email must contain @")
    
    username = email.split("@")[0]
    if len(username) < USERNAME_MIN_LENGTH:
        raise NameTooShortError(f"Name must be more than {USERNAME_MIN_LENGTH - 1} characters")
    
    if not any(email.endswith(tld) for tld in ALLOWED_DOMAINS):
        # Here we don't handle `username@tld`
        # i.e. `myuser@.net`
        raise InvalidDomainError("Domain must be one of the following: " + ", ".join(ALLOWED_DOMAINS))
    
    print("Email is valid")