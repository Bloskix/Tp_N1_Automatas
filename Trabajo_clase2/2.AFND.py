#Automata Finito No Determinista: (aa|b)*(a|bb)*
def evaluate():
    string = input("Ingrese una cadena: ")
    text = list(string)
    status = 1
    for i in string:
        if status == 1:
            if i == "a":
                status = 2
            elif i == "b":
                status = 4
            elif i == " ":
                status = 5
            else:
                print("la cadena no es valida")
                break
        if status == 2:
            if i == "a":
                status = 3
            else:
                print("la cadena no es valida")
                break
        if status == 3:
            if i == " ":
                status = 5
            else:
                print("la cadena no es valida")
                break
        if status == 4:
            if i == " ":
                status = 5
            else:
                print("la cadena no es valida")
                break
        if status == 5:
            if i == "a":
                status = 6
            elif i == " ":
                status = 9
            elif i == "b":
                status = 7
            else:
                print("la cadena no es valida")
                break
        if status == 6:
            if i == " ":
                status = 9
            else:
                print("la cadena no es valida")
                break
        if status == 7:
            if i == "b":
                status = 8
            else:
                print("la cadena no es valida")
                break
        if status == 8:
            if i == " ":
                status = 9
            else:
                print("la cadena no es valida")
                break
    if status == 9:
        print("La cadena es válida")
    else:
        pass

