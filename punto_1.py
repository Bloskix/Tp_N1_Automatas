def validate_string(string):
    list = []
    for character in string:
        character = character.isalnum()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
    list = []
    for character in string:
        character = character.isalpha()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
    list = []
    for character in string:
        character = character.isupper()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
    list = []
    for character in string:
        character = character.islower()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
    list = []
    for character in string:
        character = character.isdigit()
        list.append(character)
    if True in list:
        print(True)
    else:
        print(False)
    if len(string) >= 8:
        print(True)
    else:
        print(False)

validate_string("xy@z")