def sequential_search(llist, n):
    found = False
    pos = None
    for i in llist:
        if i == n:
            found = True
            pos = llist.index(i)
            break

    return pos

numbers = [7, 8, 5, 2, 20, 4, 92, 19]
print(sequential_search(numbers, 7))