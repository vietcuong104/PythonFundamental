def pyramid_pattern(n):  # n is the height of pyramid
    a = 2 * n - 2  # cause number of characters at the last line is 2n-1
    for i in range(0, n):
        for j in range(0, a):
            print(end=" ")
        a = a - 1
        for k in range(0, i + 1):
            print("*", end=" ")

        print("\r")


pyramid_pattern(10)
