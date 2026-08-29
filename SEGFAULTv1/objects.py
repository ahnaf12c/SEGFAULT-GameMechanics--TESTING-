import sys
import os
import GameEngine
import assets


class Keycard:
    def __init__(self, cardID, name):
        self.ID = cardID
        self.name = name
        self.unlocks = {
                'inRoom': '', #roomID
                'object': '' #objectID}
        self.location = {
                'inRoom': '', #roomID
                'inWhat': '' #storageID}

class Terminal:
    def __init__(self, termID, name):
        self.ID = termID
        self.name = name
        self.location = ''  #roomID
        self.unlockedBy = '' #keycardID

class StorageUnit:
    def __init__(self, storageID, name):
        self.ID = storageID
        self.name = name
        self.stores = []
        sel.location = '' #roomID        
