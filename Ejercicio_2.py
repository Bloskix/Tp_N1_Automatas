
def solve(operation):
    chars = '0123456789+*() '    #si se encuentra un caracter no permitido, se genera un error.
    if not all(c in chars for c in operation):    # si no cumple com estas condiciones, se genera un error , la letra c toma el valor de cada variable
        raise ValueError("Operación matemática no válida.")  # raise nos genera un error intencional
    result = eval(operation) # evaluar una cadena de texto que representa una operación matemática.
    return result
print(solve("7 + 5 * 4"))
print(solve("3+ 3 + 8"))
print(solve("1+ 5 * 9"))

