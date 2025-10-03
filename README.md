# DiceGame
### Simple Python Console Dice Rolling Game

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-success)

A straightforward console-based dice game where players roll two six-sided dice and track their highest score across multiple rounds.

## Screenshots

> **Note:** Console output screenshots will be added soon. Run `python cc_for_loop.py` to see the game in action.

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

## Prerequisites

- **Python**: version 3.6 or higher ([Download](https://www.python.org/downloads/))
- **No external dependencies required** - uses only Python's built-in `random` module

To check your Python version:
```bash
python --version
# or
python3 --version
```

## Troubleshooting

### Common Issues

**Issue:** `python: command not found`

**Solution:** Install Python 3 from [python.org](https://www.python.org/downloads/) or use `python3` instead of `python`.

---

**Issue:** Game exits immediately without showing menu

**Solution:** Ensure you're running the correct file (`python cc_for_loop.py`) and check that the file hasn't been modified.

---

**Issue:** Invalid input causes errors

**Solution:** Enter only `1` or `2` when prompted. The game expects numeric input.

---

**Issue:** Random results seem predictable

**Solution:** Python's `random` module uses a pseudorandom number generator. For true randomness in production applications, consider using `secrets` module.

For additional help, please open an issue in the repository issue tracker.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Enhancement Ideas
- Add difficulty levels
- Track statistics (average roll, total rolls, etc.)
- Implement multiple players
- Add sound effects
- Create a GUI version

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact & Support

- **Author**: Jose Santiago Echevarria
- **Issues**: Please report bugs via the repository issue tracker
- **Educational Purpose**: This project demonstrates Python loops, conditionals, and random number generation
