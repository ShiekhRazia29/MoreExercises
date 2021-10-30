
import random
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
player = False
computer_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer_choice:
        print("Tie!")
    elif(player == "Rock") and (computer_choice == "Paper") :
        if computer_choice == "Paper":
            print("You lose!", computer_choice, "covers", player)
            computer_score+=1
        else:
            print("You win!", player, "smashes", computer_choice)
            player_score+=1
    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player)
            computer_score+=1
        else:
            print("You win!", player, "covers", computer_choice)
            player_score+=1
    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose...", computer_choice, "smashes", player)
            computer_score+=1
        else:
            print("You win!", player, "cut", computer_choice )
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{computer_score}")
        print(f"Player:{player_score}")
        break