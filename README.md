 Rock Paper Scissors Game

A simple Rock Paper Scissors game built with Python.

## How to run
1. Install Python
2. Run: python rock-paper-sissors.py

## How it works:
Line 1 — import random

Brings in Python's random module so the computer can pick randomly.

The comment block

Just notes for the programmer. Python ignores it. It says rock=1, paper=2, scissors=3.

computer = random.choice([1, 2, 3])

Computer randomly picks 1, 2, or 3. That's its move.

youdict = {"r": 1, "p": 2, "s": 3}

A dictionary that converts your letter input into a number.

So if you type r → it becomes 1 (rock).

youstr = input("Enter your choice : ")

Asks YOU to type r, p, or s.

if youstr not in youdict: exit(...)

If you type something random like x or z — it immediately stops the game and shows an error. Smart validation.

reversedict = {1: "rock", 2: "paper", 3: "scissors"}

Converts numbers back to words for printing. So 1 → "rock".

you = youdict[youstr]

Converts your letter into a number. So "r" becomes 1.

print(f"you chose... computer chose...")

Shows both choices in plain English.

The big if-elif block

Checks every possible combination of computer vs you and prints the result. 9 combinations total:

3 draws (both same)
3 you win
3 you lose
