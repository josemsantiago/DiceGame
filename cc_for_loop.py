import random

def dicegame():
    high_score = 0
    while True:
        print("Current High Score: ",high_score)
        print("1. Roll Dice")
        print("2. Leave Game")

        choice = input("Enter your choice: ")

        if choice == "1":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2

            print("\nYou rolled a ... ", dice1)
            print("You rolled a ... ", dice2,"\n")
            print("You rolled a total of ", total,"\n")

            if total > high_score:
                high_score = total
                print("New high score!\n")
        elif choice == "2":
            print("Goodbye!")
            break

dicegame()