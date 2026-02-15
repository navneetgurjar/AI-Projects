#!/usr/bin/env python3
"""A small terminal-based number guessing game."""

from __future__ import annotations

import random


def choose_difficulty() -> tuple[int, int]:
    """Return (max_number, attempts) based on user difficulty selection."""
    options = {
        "easy": (10, 5),
        "medium": (25, 6),
        "hard": (50, 7),
    }

    while True:
        choice = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if choice in options:
            return options[choice]
        print("Invalid choice. Please type easy, medium, or hard.")


def play() -> None:
    print("🎮 Welcome to Guess Quest!")
    print("I'm thinking of a number. Can you find it?")

    max_number, attempts = choose_difficulty()
    secret = random.randint(1, max_number)

    print(f"\nI picked a number from 1 to {max_number}.")
    print(f"You have {attempts} attempts. Good luck!\n")

    for attempt in range(1, attempts + 1):
        raw_guess = input(f"Attempt {attempt}/{attempts} - Your guess: ").strip()

        if not raw_guess.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(raw_guess)

        if guess < 1 or guess > max_number:
            print(f"Stay in range! Enter a number from 1 to {max_number}.")
            continue

        if guess == secret:
            print(f"✅ You win! The number was {secret}.")
            return

        if guess < secret:
            print("Too low ⬆️")
        else:
            print("Too high ⬇️")

    print(f"❌ Out of attempts! The number was {secret}.")


if __name__ == "__main__":
    play()
