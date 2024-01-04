def find_duplicates(x):
    duplicates = []
    for i in range(len(x)):
        n = i + 1
        for j in range(n,len(x)):
            if (x[i] == x[j]) and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates

myList = ["christ", "lam", "giang", "mai linh", "ken", "lam", "amanda", "christ", "ken nguyen", "mai linh"]

print(find_duplicates(myList))