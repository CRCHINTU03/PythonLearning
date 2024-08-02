
import random

for i in range(5): # would run the game for 5 times .. we can use true while loop to run the loop for n number of times
    
    # we get the computers choice 
    optionsChoice = ['rock','paper','scissors']
    computerChoice = random.choice(optionsChoice)
   
   # intially we declare player choice as none 
    playerChoice = None
    
    # condition would make sure that player should only select the options from the options choice
    while playerChoice not in optionsChoice:
        playerChoice = input("Enter your choice: ").lower()

    # win conditions of the game 
    if playerChoice == computerChoice:
        print("computer: ", computerChoice)
        print("player: ", playerChoice)
        print(f"The computer choice {computerChoice} is equal to the players choice {playerChoice} so it is a TIE")

    elif playerChoice == "rock" and computerChoice == "scissors":
        print("computer: ", computerChoice)
        print("player: ", playerChoice)
        print(f"The computer choice : {computerChoice} loses to player choice: {playerChoice} so it is a WIN")
    elif playerChoice == "paper" and computerChoice == "rock":
        print("computer: ", computerChoice)
        print("player: ", playerChoice)
        print(f"The computer choice : {computerChoice} loses to player choice: {playerChoice} so it is a WIN")
    elif playerChoice == "scissors" and computerChoice == "paper":
        print("computer: ", computerChoice)
        print("player: ", playerChoice)
        print(f"The computer choice : {computerChoice} loses to player choice: {playerChoice} so it is a WIN")
    
    # cases where the computer wins
    else:
        print("computer: ", computerChoice)
        print("player: ", playerChoice)
        print(f"The computer choice : {computerChoice} wins to player choice: {playerChoice} so it is a LOSE")
    

    # condition to run the loop again if player selects yes .. 
    playAgain = input("Play again? (yes/no): ").lower()

    if playAgain != "yes":
        break

print("bye")












