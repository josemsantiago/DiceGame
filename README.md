# DiceGame
### Simple Python Console Dice Rolling Game

A straightforward console-based dice game where players roll two six-sided dice and track their highest score across multiple rounds.

## Overview

This simple Python game demonstrates basic programming concepts including loops, conditionals, random number generation, and user input handling. Players can repeatedly roll dice and the game tracks their highest total score.

## Features

- **Two Dice Rolling**: Simulates rolling two standard six-sided dice
- **High Score Tracking**: Maintains and displays the highest score achieved
- **Interactive Menu**: Simple menu system with roll dice and exit options
- **Continuous Play**: Players can roll multiple times until they choose to exit

## How to Play

1. Run the game: `python cc_for_loop.py`
2. Choose option 1 to roll dice
3. View your dice results and total score
4. If you beat your high score, it will be updated
5. Choose option 2 to exit the game

## Technical Details

- **Language**: Python 3
- **Dependencies**: Only uses Python's built-in `random` module
- **Input**: Simple text-based menu choices (1 or 2)
- **Output**: Console text showing dice results and scores

## Code Structure

```python
def dicegame():
    # Main game loop with high score tracking
    # Menu system for user interaction
    # Dice rolling with random.randint(1, 6)
```

## Sample Output

```
Current High Score:  0
1. Roll Dice
2. Leave Game
Enter your choice: 1

You rolled a ...  4
You rolled a ...  6

You rolled a total of  10

New high score!
```

## Requirements

- Python 3.x
- No external dependencies required

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
