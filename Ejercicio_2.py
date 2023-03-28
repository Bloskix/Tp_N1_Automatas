def solve(count):
    add = []
    numbers = count.split("+")
    for number in numbers:
        if number.isdigit():
            add.append(int(number))
        else:
            mult = []
            mult = number.split("*")
            result = 1
            for element in mult:
                result *= int(element)
            add.append(result)
    final_result = sum(add)
    print(final_result)

solve("2*2*2+32*2")