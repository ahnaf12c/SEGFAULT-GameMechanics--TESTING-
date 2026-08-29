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


if __name__ == '__main__':
    p = Player()
    p.location = '00'

    p.move()

    while True:
        cmd = input('>')

        if cmd.upper() == 'Q':
            break
        
        p.move(cmd)

