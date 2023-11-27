from time import time
start = time()

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]


def find_missing_number(llist):
    output = []
    numbers = set(llist)
    n = len(llist)
    for i in range(1, llist[-1]):
        if i not in numbers:
            output.append(i)

    return output


find_missing_number(listOfNumbers)
end = time()

executionTime = end - start
print("Execution time is: ", executionTime)
