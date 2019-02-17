import sys
import math

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
            
def calc_pos(rounds, position, last_pos):
    x = position[0] + rounds * (position[0] - last_pos[0])
    y = position[1] + rounds * (position[1] - last_pos[1])
    return [x, y]
    
class Player:
    def __init__(self):
        self.totalCheckpoints = 0
        self.nextCheckpointId = None
        self.x = None
        self.y = None
    
    def update_values(self):
        lastCheckpoint = self.nextCheckpointId
        self.x, self.y, self.vx, self.vy, self.angle, self.nextCheckpointId = [int(i) for i in input().split()]
        if lastCheckpoint != self.nextCheckpointId:
            self.totalCheckpoints += 1
        
    def print_output(self):
        print("{0} {1} {2}".format(
            checkpoint_list[self.nextCheckpointId][0], checkpoint_list[self.nextCheckpointId][1], 100))

# 
checkpoint_list = []
laps = int(input())
checkpointCount = int(input())
for _ in range(checkpointCount):
    checkpoint_list.append([int(i) for i in input().split()])

player1 = Player()
player2 = Player()
opponent1 = Player()
opponent2 = Player()

# game loop
while True:
    player1.update_values()
    player2.update_values()
    opponent1.update_values()
    opponent2.update_values()
    

    player1.print_output()
    player2.print_output()
    