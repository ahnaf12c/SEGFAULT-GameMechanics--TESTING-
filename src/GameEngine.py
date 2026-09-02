import sys
import os
import time
import sys, tty, termios

def get_char():
    if sys.platform == "win32":
        import msvcrt
        return msvcrt.getch().decode("utf-8", errors="ignore").lower()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deleteLastLines(n=1):
    """Clears a specified number of lines above the cursor."""
    for _ in range(n):
        # Move cursor up 1 line, delete to end of line
        print("\033[F\033[K", end="")

def deleteCurrentLine():
    print("\r\033[K", end = '')

def hideCursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def showCursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()


if __name__ == '__main__':
    char = get_char()
    print(char)
