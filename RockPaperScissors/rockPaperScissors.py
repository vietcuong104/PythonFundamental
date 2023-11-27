import random


def gameplay():
    player1 = input("Select Paper, Rock or Scissors: ").lower()
    player2 = random.choice(["Paper", "Rock", "Scissors"]).lower()

    print("Player 2 choice is:", player2)

    if (player1 == 'paper') and (player2 == 'scissors'):
        print("Player 2 Win")
    elif (player1 == 'rock') and (player2 == 'paper'):
        print("Player 2 Win")
    elif (player1 == 'scissors') and (player2 == 'rock'):
        print("Player 2 Win")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 1 Win")


gameplay()
