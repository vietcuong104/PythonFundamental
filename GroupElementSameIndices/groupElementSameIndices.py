inputLists = [[17, 8, 15], [25, 11, 92], [23, 12, 21], [66, 77, 88]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[i].append(inputLists[j][i])

print(outputLists)
