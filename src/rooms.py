import os
import sys
import time
import GameEngine
import assets

tiles = assets.TILES


class Room:
    def __init__(self, roomID, name):
        self.ID = roomID
        self.name = name
        self.matrix = []
        self.keyItems = {}
        self.interactables = {}
        self.exits = {}
        self.state = {}
        self.is_Locked = {}
        self.commands = []
    def render(self):
        GameEngine.clearScreen()
        print(self.name)
        for row in self.matrix:
            for cell in row:
                print(tiles[cell], end = '')
            print()
        
if __name__ == '__main__':
    test = Room("room01", "testRoom")
    test.matrix = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,4,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,1,1,3,3,3,3,3,1,1,1,1,1]]
    test.interactables = {"terminal": "Hello There!"}
    test.exits = {"N": "room3",
               "S": "room2"}
    test.is_Locked = {
            "N": False,
            "S": True,
            "terminal": False}
    test.commands = list(test.interactables.keys()) + list(test.exits.keys()) + ['inspect']

    GameEngine.clearScreen()
    test.render()

    while True:
        out = input(">")

        if out == 'q':
            break
        elif out == 'unlock':
            test.is_Locked["S"] = False
            GameEngine.clearScreen()
            print("Unlocking. . .")
            time.sleep(2)
            print("Unlocked!")
            time.sleep(2)
            for i in range(5, 10):
                test.matrix[10][i] = 2
            GameEngine.clearScreen()
            test.render()
            continue
        elif out not in test.commands:
            GameEngine.deleteLastLines(1)
            continue
        elif out == 'inspect':
            back = input(list(test.interactables.keys()))
            GameEngine.deleteLastLines(2)
            continue
        else:
            time.sleep(2)
            GameEngine.deleteLastLines()
            continue
