import os
import time
import sys
import GameEngine
import rooms
import world


class Player:
    def __init__(self):
        self.location = ""
        self.inventory = []

    def move(self, direction = ''):
        d = direction.upper()
        if d in world.WORLD[self.location].exits and world.WORLD[self.location].is_Locked[d] == True:
            GameEngine.clearScreen()
            print('Area Locked!')
            time.sleep(2)

        elif d in world.WORLD[self.location].exits:
            self.location = world.WORLD[self.location].exits[d]
        
        world.WORLD[self.location].render()

    def showInv(self):
        GameEngine.clearScreen()
        print("\033[1;32mPLAYER INVENTORY:\033[0m\n")
        if len(self.inventory) == 0:
            print("\033[1;31mEMPTY!\n\033[0m")
        for i in range(0, len(self.inventory)):
            print(f"\033[1m[{i+1}]: {self.inventory[i]}\033[0m" if len(self.inventory) != 0 else "")

        q = GameEngine.get_char()
        if q == 'i':
            GameEngine.clearScreen()
            self.move()
            return

    def inspect(self):
        GameEngine.clearScreen()
        r = world.WORLD[self.location]
        print(f"\033[1;32m{r.name}: \033[0m\n")
        if len(r.interactables) == 0:
            print("\033[1;31mNothing too special here. Just an empty room.\n\033[0m")
        for i in range(0, len(r.interactables)):
            print(f"\033[1m[{i+1}]: {list(r.interactables.keys())[i]}\033[0m" if len(r.interactables) != 0 else "")

        q = GameEngine.get_char()
        if q == 'l':
            GameEngine.clearScreen()
            self.move()
            return 
        
        

MOVECMD = {
        'w': 'N',
        'a': 'W',
        's': 'S',
        'd': 'E'}




if __name__ == '__main__':
    p = Player()
    p.location = '00'

    p.move()
    GameEngine.hideCursor() 

    while True: 
        cmd = GameEngine.get_char()

        if cmd == 'q':
            GameEngine.showCursor()
            break

        elif cmd == 'i':
            p.showInv()

        elif cmd == 'l':
            p.inspect()

        elif cmd in MOVECMD:
            p.move(MOVECMD[cmd])
            time.sleep(0.15)
