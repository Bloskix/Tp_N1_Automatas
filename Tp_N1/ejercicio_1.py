import re

def email_checker(email):
    email_form = "^([a-zA-Z]([a-zA-Z0-9\.\_\-]*[a-z0-9]))@([a-z0-9]([a-zA-Z0-9-]*[a-z0-9]))+(\.(com|nav|gov|net|org))+(\.(ar|mx|es|us|pr))?$"

    if re.fullmatch(email_form, email):
        print(f'El mail \"{email}\" es correcto')
    else:
        print(f'El mail \"{email}\" es incorrecto')

with open("ejercicio_1.txt", "r") as file:
    content = [file.read()]
    content = content[0].split("\n")

for mail in content:
    email_checker(mail)