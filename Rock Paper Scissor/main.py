"""
Workflow of project:
1- iput from user(rock, paper, scissor)
2- computer will choose randomly not conditionally) #random module
3- result print

Cases:

 A- Rock
 Rock - Rock = Tie
 Rock - paper = Paper win
 Rock - scissor = Rock win

B- Paper
 Paper - Paper = Tie
 Paper - Rock = Paper win
 Paper - Scissor = Scissor win

C- Scissor
 Scissor - Scissor = Tie
 Scissor - Rock = Rock win
 Scissor - Paper = Scissor win


"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_wins = 0
computer_wins = 0

while True:
    user_choice = input("Enter your move (Rock, Paper, Scissor) or 'quit': ").strip().capitalize()
    
    if user_choice == "Quit":
        print(f"\nFinal Score - You: {user_wins} | Computer: {computer_wins}")
        break
    
    if user_choice not in item_list:
        print("Invalid move! Try again.\n")
        continue
    
    comp_choice = random.choice(item_list)

    print(f"User choice: {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Tie\n")

    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock = computer win")
            computer_wins += 1
        else:
            print("Rock smashes Scissor = You win")
            user_wins += 1

    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts paper, Computer win")
            computer_wins += 1
        else:
            print("Paper covers rock, you win")
            user_wins += 1

    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissor cuts paper, you win")
            user_wins += 1
        else:
            print("Rock smashes Scissor, Computer win")
            computer_wins += 1
    
    print(f"Score: You {user_wins} - Computer {computer_wins}\n")

