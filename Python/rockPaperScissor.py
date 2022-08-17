#create a game of Rock Paper Scissor 
# keep track of the score
import random

def rockPaperScissor(yourScore, computerScore):
    print("Rock Paper Scissor")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You chose Rock")
    elif choice == 2:
        print("You chose Paper")
    elif choice == 3:
        print("You chose Scissor")
    elif choice == 4:
        print("Exiting")
        return
    else:
        print("Invalid choice")
        rockPaperScissor(yourScore, computerScore)
    computerChoice = random.randint(1,3)
    if computerChoice == 1:
        print("Computer chose Rock")
    elif computerChoice == 2:
        print("Computer chose Paper")
    elif computerChoice == 3:
        print("Computer chose Scissor")

    if choice == computerChoice:
        print("It's a tie")
    elif choice == 1 and computerChoice == 2:
        print("You win")
        yourScore += 1
    elif choice == 1 and computerChoice == 3:
        print("You lose")
        computerScore += 1
    elif choice == 2 and computerChoice == 1:
        print("You lose")
        computerScore += 1
    elif choice == 2 and computerChoice == 3:
        print("You win")
        yourScore += 1
    elif choice == 3 and computerChoice == 1:
        print("You win")
        yourScore += 1
    elif choice == 3 and computerChoice == 2:
        print("You lose")
        computerScore += 1
    print("Your score: ", yourScore)
    print("Computer score: ", computerScore)
    print('\n')
    rockPaperScissor(yourScore, computerScore)

yourScore = 0
computerScore = 0
rockPaperScissor(yourScore, computerScore)