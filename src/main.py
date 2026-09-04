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

intro.titlePageInput()

wmap = world.WORLD

plr = player.Player()

startLocation = '00'
plr.location =  startLocation
inv = plr.inventory


