def maximum(x):
    max_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] > x[max_index]:
            max_index = current_index
        current_index = current_index + 1
    return max_index


mylist = [8, 11, 67, 45, 33, 19, 5]
print(maximum(mylist))
