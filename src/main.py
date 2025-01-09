#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## main.py
## File description:
## main
##

import sys
from Gomoku import play

def main():
    try:
        if play() != 0:
            sys.exit(84)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(84)
    sys.exit(0)

if __name__ == "__main__":
    main()
