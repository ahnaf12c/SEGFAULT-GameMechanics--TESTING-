import GameEngine
import rooms
import assets
import objects

matrices = assets.ROOM_MATRICES

#EntryHub
entryHub = rooms.Room("00", "Entry Hub")
entryHub.matrix = matrices[entryHub.ID]
entryHub.exits = {
        'N': '03',
        'W': '01',
        'E': '02',
        'S': '04'}
entryHub.interactables = {
        'MysteryNote': '0001'}
entryHub.is_Locked = {
        'N': True,
        'W': False,
        'E': False,
        'S': False
        }
entryHub.keyItems = {
        'redKeycard': 'N'}

#StorageCloset
storageCloset = rooms.Room("01", "Storage Closet")
storageCloset.matrix = matrices[storageCloset.ID]
storageCloset.exits = {
        'E': '00'}
storageCloset.interactables = {
        'ST0101': ['Red Keycard'],
        'ST0102': [],
        'ST0103': [],
        'ST0104': []}
storageCloset.is_Locked = {
        'E': False}

#ResearchLab
researchLab = rooms.Room("02", "Research Lab")
researchLab.matrix = matrices[researchLab.ID]
researchLab.exits = {
        'W': '00'}
researchLab.is_Locked = {
        'W': False}

#SecurityRoom
securityRoom = rooms.Room("03", "Security Room")
securityRoom.matrix = matrices[securityRoom.ID]
securityRoom.exits = {
        'S': '00'}
securityRoom.is_Locked = {
        'S': False}

#CourtYard
courtyard = rooms.Room("04", "Courtyard")
courtyard.matrix = matrices[courtyard.ID]
courtyard.exits = {
        'N': '00'}
courtyard.is_Locked = {
        'N': False}

WORLD = {
    entryHub.ID: entryHub,
    storageCloset.ID: storageCloset,
    researchLab.ID: researchLab,
    securityRoom.ID: securityRoom,
    courtyard.ID: courtyard,
}


"""OBJECTS AND INTERACTABLES IN THE MAP"""

#StorageUnits

unit1 = objects.StorageUnit('ST0101', 'Unit1')
unit1.location = '01'
unit1.stores = WORLD[unit1.location].interactables[unit1.ID]


#Keycards
redkeycard = objects.Keycard(assets.ITEMS['redKeycard']['ID'], assets.ITEMS['redKeycard']['name'])
redkeycard.unlocks['inRoom'] = '00'
redkeycard.unlocks['object'] = 'N'
redkeycard.location['inRoom'] = '01'
redkeycard.location['inWhat'] = 'ST0101'

#Doors
ehN = objects.Door('N', 'Entry Hub North Door')
ehN.room = '00'
ehN.locked = True
ehN.coordsInRoom = [[0,5], [0,6], [0,7], [0,8]]
