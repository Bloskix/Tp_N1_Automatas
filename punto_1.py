def validate_string(string):
    print(any(character.isalnum() for character in string))
    print(any(character.isalpha() for character in string))
    print(any(character.isupper() for character in string))
    print(any(character.islower() for character in string))
    print(any(character.isdigit() for character in string))
    print(len(string) >= 8)
validate_string("xy@z")

