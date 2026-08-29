import GameEngine
import rooms
import assets

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
        'Storage': '0001'}
entryHub.is_Locked = {
        'N': True,
        'W': False,
        'E': False,
        'S': False,
        'Storage': False}
entryHub.keyItems = {
        'redKeycard': 'N'}

#StorageCloset
storageCloset = rooms.Room("01", "Storage Closet")
storageCloset.matrix = matrices[storageCloset.ID]
storageCloset.exits = {
        'E': '00'}
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
