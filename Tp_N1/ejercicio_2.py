import re

def URL_checker(url):
    url_form = "^((http:\/\/|https:\/\/)?)((www\.)?)([a-zA-Z0-9]+)(\.(com))(\/[a-zA-Z0-9]+)*(\/)?((\?)[a-zA-Z0-9]+(=)[a-zA-Z0-9]+)?$"

    if re.fullmatch(url_form, url):
        print(f"La URL \"{url}\" es valida")
    else:
        print(f"La URL \"{url}\" no es valida")

with open("ejercicio_2.txt", "r") as file:
    content = [file.read()]
    content = content[0].split("\n")

for url in content:
    URL_checker(url)