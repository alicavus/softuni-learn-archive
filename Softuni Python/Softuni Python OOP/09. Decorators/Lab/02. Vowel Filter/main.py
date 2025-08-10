def vowel_filter(function):

    def wrapper():
        vowels = "aeouiy"
        return [char for char in function() if char in vowels]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())