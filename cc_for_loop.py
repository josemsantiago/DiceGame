#!/usr/bin/env python3
"""
DiceGame - Simple Console Dice Rolling Game
Roll two dice and track your highest score!
"""

import random
import sys

def roll_dice():
    """Roll two six-sided dice and return the results."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def display_menu(high_score):
    """Display the game menu with current high score."""
    print(f"\n{'='*30}")
    print(f"Current High Score: {high_score}")
    print(f"{'='*30}")
    print("1. Roll Dice")
    print("2. Leave Game")
    print(f"{'='*30}")

def get_user_choice():
    """Get and validate user menu choice."""
    try:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return None
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Goodbye!")
        return "2"
    except Exception as e:
        print(f"An error occurred while getting input: {e}")
        return None

def display_roll_result(dice1, dice2, total, is_new_high_score=False):
    """Display the results of a dice roll."""
    print("\n" + "="*25)
    print("DICE ROLL RESULTS")
    print("="*25)
    print(f"Die 1: {dice1}")
    print(f"Die 2: {dice2}")
    print(f"Total: {total}")

    if is_new_high_score:
        print("🎉 NEW HIGH SCORE! 🎉")
    print("="*25)

def dicegame():
    """Main dice game function."""
    print("Welcome to the Dice Game!")
    print("Roll two dice and try to get the highest score possible!")

    high_score = 0

    try:
        while True:
            display_menu(high_score)
            choice = get_user_choice()

            if choice is None:
                continue  # Invalid input, show menu again

            if choice == "1":
                # Roll the dice
                dice1, dice2 = roll_dice()
                total = dice1 + dice2

                # Check for new high score
                is_new_high_score = total > high_score
                if is_new_high_score:
                    high_score = total

                # Display results
                display_roll_result(dice1, dice2, total, is_new_high_score)

            elif choice == "2":
                print(f"\nThanks for playing!")
                if high_score > 0:
                    print(f"Your final high score was: {high_score}")
                print("Goodbye!")
                break

    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        if high_score > 0:
            print(f"Your final high score was: {high_score}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Thanks for playing!")

def main():
    """Main entry point for the dice game."""
    try:
        dicegame()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()