with open("demo.txt", "r") as f:
    count = 0
    text = f.read()
    for i in text:
        if i.isupper():
            print(i)
            count = count + 1
    print(count)


