import numpy as np

def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:]) # index of the min value in list
        x[i], x[swap] = x[swap], x[i]

    return x

llist = [7, 8, 5, 2, 20, 4, 92]
print(sorting(llist))