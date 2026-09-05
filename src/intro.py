import os
import sys
import time
import random
import GameEngine
import assets

TITLE = f"""\033[1;32m

 █████████═╗ █████████═╗   ████████═╗ █████████═╗ ███████═╗   ██═╗   ██═╗ ██═╗    ██████████═╗ 
 ██ ╔══════╝ ██ ╔══════╝ ██ ╔═══════╝ ██ ╔══════╝ ██ ╔═══██═╗ ██ ║   ██ ║ ██ ║     ╚══██ ╔═══╝
 ██ ║        ██ ║        ██ ║         ██ ║        ██ ║   ██ ║ ██ ║   ██ ║ ██ ║        ██ ║   
 █████████═╗ ██████═╗    ██ ║ █████═╗ ███████═╗   █████████ ║ ██ ║   ██ ║ ██ ║        ██ ║
        ██ ║ ██ ╔═══╝    ██ ║  ╚═██ ║ ██ ╔════╝   ██ ╔═══██ ║ ██ ║   ██ ║ ██ ║        ██ ║  
        ██ ║ ██ ║        ██ ║    ██ ║ ██ ║        ██ ║   ██ ║ ██ ║   ██ ║ ██ ║        ██ ║  
 ███████ ╔═╝ █████████═╗   ██████ ╔═╝ ██ ║        ██ ║   ██ ║ ███████ ╔═╝ █████████═╗ ██ ║       
  ╚══════╝    ╚════════╝    ╚═════╝    ╚═╝         ╚═╝    ╚═╝  ╚══════╝    ╚════════╝  ╚═╝

                                        [BETA TESTING]
\033[0m"""

TITLECORRUPTED = f"""\033[1;32m

  █████████═╗ █████████═╗   ████████═╗ █████████═╗ ███████═╗   ██═╗   ██═╗██═╗     ██████████═╗ 
 ██ ╔══════╝ ██ ╔══════╝ ██ ╔═══════╝ ██ ╔══════╝ ██ ╔═══██═╗ ██ ║   ██ ║ ██ ║     ╚══██ ╔═══╝
 ██ ║        ██ ║        ██ ║         ██ ║        ██ ║   ██ ║ ██ ║   ██ ║  ██ ║       ██ ║   
  █████████═╗ ██████═╗    ██ ║ █████═╗ ███████═╗   █████████  ██ ║   ██ ║ ██ ║         ██ ║
        ██ ║ ██ ╔═══╝    ██ ║  ╚═██ ║ ██ ╔════╝   ██ ╔═══██ ║  ██ ║   ██ ║██ ║        ██ ║  
        ██ ║ ██ ║        ██ ║    ██ ║ ██ ║        ██ ║   ██ ║ ██ ║   ██ ║  ██ ║        ██ ║  
███████ ╔═╝ █████████═╗   ██████ ╔═╝ ██ ║        ██ ║   ██ ║  ███████ ╔═╝  █████████═╗ ██ ║       
  ╚══════╝    ╚════════╝    ╚═════╝    ╚═╝         ╚═╝    ╚═╝  ╚══════╝    ╚════════╝  ╚═╝

\033[0m"""

MENU = """\033[1;97m
                                [1]: START GAME

                                [2]: HELP & CONTROLS
                                
                                [3]: NOTES FROM ME

                                [4]: QUIT GAME\033[0m

                                \033[97mPress a key...\033[0m
"""
 
def titlePage():
    GameEngine.clearScreen()
    print(TITLE)
    print(MENU)

def titlePageInput(): 
    while True:
        titlePage() 
        i = GameEngine.get_char()
        match i:
            case '1':
                GameEngine.clearScreen()
                break
            case '2':
                GameEngine.clearScreen()
                print(assets.HELP_TEXT)
                print("Press any key...")
                q = GameEngine.get_char()
                continue
            case '3':
                pass
            case '4':
                GameEngine.clearScreen()
                print("\033[1mDo you want to exit the game? [y/n]\033[0m")
                q = GameEngine.get_char()
                match q:
                    case 'y':
                        print("Exiting Game...")
                        time.sleep(3)
                        GameEngine.clearScreen()
                        sys.exit()
                    case 'n':
                        continue


if __name__  ==  '__main__':
    #titlePage()
    titlePageInput()

