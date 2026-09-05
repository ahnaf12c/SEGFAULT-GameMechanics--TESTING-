import os
import sys
import time
import assets
import rooms
import objects
import GameEngine
import world
import player
import intro

wmap = world.WORLD

plr = player.Player()

startLocation = '00'
plr.location =  startLocation
inv = plr.inventory

while True:
    GameEngine.showCursor() 
    intro.titlePageInput()
    plr.move()

    GameEngine.hideCursor() 
 
    while True:
        cmd = GameEngine.get_char()
    
        if cmd == 'q':
            break

        elif cmd == 'i':
            plr.showInv()

        elif cmd == 'l':
            plr.inspect()
 

        elif cmd in player.MOVECMD:
            plr.move(player.MOVECMD[cmd])
            time.sleep(0.15) 

