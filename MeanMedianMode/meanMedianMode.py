list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]


def mean(mylist):
    mean = sum(mylist) / len(mylist)
    return mean

def median(mylist):
    mylist.sort()
    if len(mylist) % 2 == 0:
        m1 = mylist[len(mylist) // 2 - 1]
        m2 = mylist[len(mylist) // 2]
        median = (m1 + m2) / 2

    else:
        median = mylist[len[mylist]//2]

    return median

def mode(mylist):
    frequency = {}
    for i in mylist:
        frequency.setdefault(i, 0)
        frequency[i] += 1

    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i

    return mode

myMean = mean(list1)
print("Mean is: ", myMean)

myMedian = median(list1)
print("Median is: ", myMedian)

myMode = mode(list1)
print("Mode is: ", myMode)
