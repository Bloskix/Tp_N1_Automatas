def validate_string(string):
    validate_isalnum(string)
    validate_isalpha(string)
    validate_isupper(string)
    validate_islower(string)
    validate_isdigit(string)
    if len(string) >= 8:
        print(True)
    else:
        print(False)

def validate_isalnum(string):
    list = []
    for character in string:
        character = character.isalnum()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
def validate_isalpha(string):
    list = []
    for character in string:
        character = character.isalpha()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
def validate_isupper(string):
    list = []
    for character in string:
        character = character.isupper()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
def validate_islower(string):
    list = []
    for character in string:
        character = character.islower()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
def validate_isdigit(string):
    list = []
    for character in string:
        character = character.isdigit()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
validate_string("xy@z")