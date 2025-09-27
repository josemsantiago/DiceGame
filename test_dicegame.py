#!/usr/bin/env python3
"""
Test suite for DiceGame
Tests dice rolling mechanics and game functions
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock
import cc_for_loop


class TestDiceGame(unittest.TestCase):
    """Test cases for DiceGame functionality."""

    def test_roll_dice_returns_valid_values(self):
        """Test that roll_dice returns valid dice values (1-6)."""
        for _ in range(100):  # Test multiple rolls
            dice1, dice2 = cc_for_loop.roll_dice()
            self.assertIn(dice1, range(1, 7))
            self.assertIn(dice2, range(1, 7))

    def test_roll_dice_returns_tuple(self):
        """Test that roll_dice returns a tuple of two values."""
        result = cc_for_loop.roll_dice()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    @patch('builtins.input', return_value='1')
    def test_get_user_choice_valid_input(self, mock_input):
        """Test get_user_choice with valid input."""
        result = cc_for_loop.get_user_choice()
        self.assertEqual(result, '1')

    @patch('builtins.input', return_value='2')
    def test_get_user_choice_exit(self, mock_input):
        """Test get_user_choice with exit choice."""
        result = cc_for_loop.get_user_choice()
        self.assertEqual(result, '2')

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_get_user_choice_invalid_then_valid(self, mock_input):
        """Test get_user_choice with invalid input followed by valid."""
        # First call should return None due to invalid input
        result1 = cc_for_loop.get_user_choice()
        self.assertIsNone(result1)

        # Second call should return valid input
        result2 = cc_for_loop.get_user_choice()
        self.assertEqual(result2, '1')

    def test_display_menu(self):
        """Test menu display function."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.display_menu(5)
            output = captured_output.getvalue()
            self.assertIn("Current High Score: 5", output)
            self.assertIn("1. Roll Dice", output)
            self.assertIn("2. Leave Game", output)
        finally:
            sys.stdout = sys.__stdout__

    def test_display_roll_result_normal(self):
        """Test display of normal roll result."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.display_roll_result(3, 4, 7, False)
            output = captured_output.getvalue()
            self.assertIn("Die 1: 3", output)
            self.assertIn("Die 2: 4", output)
            self.assertIn("Total: 7", output)
            self.assertNotIn("NEW HIGH SCORE", output)
        finally:
            sys.stdout = sys.__stdout__

    def test_display_roll_result_high_score(self):
        """Test display of high score roll result."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.display_roll_result(6, 6, 12, True)
            output = captured_output.getvalue()
            self.assertIn("Die 1: 6", output)
            self.assertIn("Die 2: 6", output)
            self.assertIn("Total: 12", output)
            self.assertIn("NEW HIGH SCORE", output)
        finally:
            sys.stdout = sys.__stdout__

    @patch('cc_for_loop.roll_dice', return_value=(3, 4))
    @patch('builtins.input', side_effect=['1', '2'])
    def test_dicegame_single_roll(self, mock_input, mock_roll):
        """Test a complete game with one roll and exit."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.dicegame()
            output = captured_output.getvalue()
            self.assertIn("Welcome to the Dice Game", output)
            self.assertIn("Die 1: 3", output)
            self.assertIn("Die 2: 4", output)
            self.assertIn("Total: 7", output)
            self.assertIn("Thanks for playing", output)
        finally:
            sys.stdout = sys.__stdout__

    @patch('cc_for_loop.roll_dice', side_effect=[(2, 3), (6, 6)])
    @patch('builtins.input', side_effect=['1', '1', '2'])
    def test_dicegame_high_score_progression(self, mock_input, mock_roll):
        """Test game with high score improvement."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.dicegame()
            output = captured_output.getvalue()
            # Should show the progression from score 5 to score 12
            self.assertIn("Total: 5", output)
            self.assertIn("Total: 12", output)
            self.assertIn("NEW HIGH SCORE", output)
            self.assertIn("Your final high score was: 12", output)
        finally:
            sys.stdout = sys.__stdout__

    @patch('builtins.input', return_value='2')
    def test_dicegame_immediate_exit(self, mock_input):
        """Test exiting game immediately."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.dicegame()
            output = captured_output.getvalue()
            self.assertIn("Welcome to the Dice Game", output)
            self.assertIn("Thanks for playing", output)
            # Should not show final high score for immediate exit
            self.assertNotIn("Your final high score was:", output)
        finally:
            sys.stdout = sys.__stdout__


class TestDiceGameEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    @patch('builtins.input', side_effect=KeyboardInterrupt)
    def test_keyboard_interrupt_handling(self, mock_input):
        """Test handling of keyboard interrupt."""
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            cc_for_loop.get_user_choice()
            output = captured_output.getvalue()
            self.assertIn("Game interrupted", output)
        finally:
            sys.stdout = sys.__stdout__

    def test_main_function_exists(self):
        """Test that main function is callable."""
        self.assertTrue(callable(cc_for_loop.main))

    def test_dice_randomness(self):
        """Test that dice rolls produce varied results over many iterations."""
        results = set()
        for _ in range(50):
            dice1, dice2 = cc_for_loop.roll_dice()
            results.add((dice1, dice2))

        # Should have some variety in results (not all the same)
        self.assertGreater(len(results), 10)

    def test_high_score_logic(self):
        """Test high score tracking logic in isolation."""
        # Simulate game logic
        high_score = 0

        # First roll
        total1 = 7
        if total1 > high_score:
            high_score = total1
        self.assertEqual(high_score, 7)

        # Lower roll shouldn't change high score
        total2 = 5
        if total2 > high_score:
            high_score = total2
        self.assertEqual(high_score, 7)

        # Higher roll should change high score
        total3 = 11
        if total3 > high_score:
            high_score = total3
        self.assertEqual(high_score, 11)


if __name__ == '__main__':
    unittest.main()