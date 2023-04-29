#Automata Finito No Determinista: (a|b)*
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
            elif i == " ":
                status = 3
            else:
                print("la cadena no es valida")
                break
        if status == 1 or status == 2:
            if i == " ":
                status = 3
            else:
                print("la cadena no es valida")
                break
        if status == 3:
            print("La cadena es válida")
        else:
            pass


