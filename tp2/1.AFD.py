#Automata Finito Determinista: (a|b)*
def evaluate():
    string = input("Ingrese una cadena: ")
    text = list(string)
    status = 0
    for i in text:
        if status == 0:
            if i == "a":
                status = 1
            elif i == "b":
                status = 2
            else:
                print("la cadena no es valida")
                break
        if status == 1:
            if i == "a":
                status = 1
            elif i == "b":
                status = 2
            else:
                print("la cadena no es valida")
                break
        if status == 2:
            if i == "a":
                status = 1
            elif i == "b":
                status = 2
            else:
                print("la cadena no es valida")
                break
    if i == len(text):
        print("La cadena es válida")
