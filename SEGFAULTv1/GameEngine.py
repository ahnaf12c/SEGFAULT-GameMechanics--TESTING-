import sys
import os
import time

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deleteLastLines(n=1):
    """Clears a specified number of lines above the cursor."""
    for _ in range(n):
        # Move cursor up 1 line, delete to end of line
        print("\033[F\033[K", end="")

def deleteCurrentLine():
    print("\r\033[K", end = '')

