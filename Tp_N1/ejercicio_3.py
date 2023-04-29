import re

def IP_checker(ip):
    ip_form = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if re.fullmatch(ip_form, ip):
        print(f"La ip \"{ip}\" es válida")
    else:
        print(f"La ip \"{ip}\" no es válida")

with open("ejercicio_3.txt", "r") as file:
    content = [file.read()]
    content = content[0].split("\n")

for ip in content:
    IP_checker(ip)
