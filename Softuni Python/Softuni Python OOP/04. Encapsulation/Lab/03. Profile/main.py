class Profile:
    __min_user_len: int = 5
    __max_user_len: int = 15
    __min_password_len: int = 8

    def __init__(self, username: str, password: str, ):
        if not Profile.__min_user_len <= len(username) <= Profile.__max_user_len:
            raise ValueError(f"The username must be between {Profile.__min_user_len} and {Profile.__max_user_len} characters.")
        if Profile.__min_password_len > len(password) or \
            not any(x.isupper() for x in password) or \
            not any(x.isdigit() for x in password):
            raise ValueError(f"The password must be {Profile.__min_password_len} or more characters with at least 1 digit and 1 uppercase letter.")
        
        self.__username = username
        self.__password = password
    
    def __str__(self) -> str:
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"

   
# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
