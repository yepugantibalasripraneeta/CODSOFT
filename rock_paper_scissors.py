import random

user_score = 0
computer_score = 0

print("=== Rock Paper Scissors Game ===")

while True:
    print("\nChoose:")
    print("rock")
    print("paper")
    print("scissors")

    user = input("Enter your choice: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break