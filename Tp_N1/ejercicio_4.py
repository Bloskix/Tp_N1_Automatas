def most_repeated_word(text):
    text = text.lower()

    words = text.split()

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    max_word = None
    max_cont = 0
    for word, cont in counts.items():
        if cont > max_cont:
            max_word = word
            max_cont = cont

    print(f"La palabra mas repetida es: \"{max_word}\", que se repite {max_cont} veces")

with open("ejercicio_4.txt", "r") as file:
    content = [file.read()]
    content = content[0].split("\n")

for text in content:
    most_repeated_word(text)