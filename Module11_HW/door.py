class Door:
    def __init__(self, number, status, lock):
        self.number = number
        self.status = status
        self.lock = lock
    def open(self):
        """Door opened"""
        if self.lock == 'unlocked':
            self.status = 'opened'
    def close(self):
        """Door closed"""
        self.status = 'closed'
    def onLock(self):
        """Door locked"""
        self.lock = 'locked'
    def unLock(self):
        """Door unlocked"""
        self.lock = 'unlocked'

door1 = Door(1, 'closed', 'unlocked')
door1.open()
print(door1.status)
door1.close()
print(door1.status)
door1.onLock()
print(door1.lock)
door1.open()
print(door1.status)
door1.unLock()
door1.open()
print(door1.status)

class ColouredDoor:
    def __init__(self, number, colour, status = 'closed'):
        self.number = number
        self.status = status
        self.colour = colour
    def open(self):
        """Door opened"""
        self.status = 'opened'
    def close(self):
        """Door closed"""
        self.status = 'closed'

cdoor1 = ColouredDoor(1, 'opened', 'black')
print(cdoor1.colour)
cdoor1.colour = 'white'
print(cdoor1.colour)
cdoor2 = ColouredDoor(2, 'orange')
print(cdoor2.colour)
cdoor2.status
print(cdoor2.status)
cdoor2.open()
print(cdoor2.status)

class ToggleDoor:
    def __init__(self, number, status):
        self.number = number
        self.status = status
        
    def toggle(self):
        """Door toggled"""
        tog_dict = {'closed': 'opened', 'opened': 'closed'}
        self.status = tog_dict[self.status]

tdoors1 = ToggleDoor(1, 'opened')
print(tdoors1.status)
tdoors1.toggle()
print(tdoors1.status)


