def recursive_binary_search(target, sequence, first, last):
    if first > last:
        return False
    else:
        mid = (last + first) // 2 # actual index of mid
        if target == sequence[mid]:
            return True
        elif target < sequence[mid]:
            return recursive_binary_search(target, sequence, first, mid-1)
        else:
            return recursive_binary_search(target, sequence, mid+1, last)


llist = [1, 3, 4, 7, 8, 9, 10, 45, 50, 90, 100, 150, 600, 1000]
print(recursive_binary_search(453, llist, 0, 13))