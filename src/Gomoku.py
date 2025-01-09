##
## EPITECH PROJECT, 2024
## Gomoku.py
## File description:
## Gomoku
##

from AI import AI

def play():
    ai = AI()
    while True:
        try:
            entry = input().strip().split()
            if not entry:
                continue
            if entry[0].upper() == "END":
                return (0)
            ai.parsing(entry)
        except EOFError:
            print("Exiting...", flush=True)
            return (0)
        except Exception as e:
            print(f"ERROR: Unexpected error occurred: {e}", flush=True)
            return (84)
