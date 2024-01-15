def minimum(x):
    min_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] < x[min_index]:
            min_index = current_index
        current_index = current_index + 1
    return min_index


mylist = [8, 11, 67, 45, 2, 33, 19, 5, 90]
print(minimum(mylist))
