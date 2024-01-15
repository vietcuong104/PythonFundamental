def least_common_multiple(a, b):
    global greater
    if a == 0 or b == 0:
        print(a, " and ", b, "has no lcm...")
        return
    if a > b:
        greater = a
    elif a < b:
        greater = b

    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater = greater + 1
    return lcm


print(least_common_multiple(9, 11))
