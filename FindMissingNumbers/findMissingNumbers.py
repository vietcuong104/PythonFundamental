def find_missing_number(list):
    output = []
    numbers = set(list)
    n = len(list)
    for i in range(1, list[-1]):
        if i not in numbers:
            output.append(i)

    return output


listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(find_missing_number(listOfNumbers))
