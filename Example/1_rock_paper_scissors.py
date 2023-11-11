import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = None
    print(computer)
    while player not in choices:
        player = input("rock, papar or scissors? :").lower()

    if player == computer:
        print("computer: " + computer)
        print("player: " + player)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("you lose")
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("you win")
    elif player == "paper":
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("you lose")
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("you win")
    elif player == "scissors":
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("you lose")
        if computer == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("you win")

    play_again = input("Play again? Y / N")
    if play_again != "Y":
        break
print("bye")
