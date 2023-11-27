import random

n = random.randrange(1,10)
guess = int(input("Enter your choices: "))

while guess != n:
    if guess < n:
        print("too low")
        guess = int(input("Enter your choices: "))
    elif guess > n:
        print("too high")
        guess = int(input("Enter your choices: "))
    else:
        break

print("Correct! The number is: ", n)
