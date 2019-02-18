import sys
import math

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def __add__(self, other):
        return Point(self.getX() + other.getX(), self.getY() + other.getY())

    def __sub__(self, other):
        return Point(self.getX() - other.getX(), self.getY() - other.getY())

    def __mul__(self, factor):
        return Point(self.getX() * factor, self.getY() * factor)

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y) 

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)

    def __abs__(self):
        return math.sqrt(self.X**2 + self.Y**2)

    
class Player:
    def __init__(self):
        self.totalCheckpoints = 0
        self.nextCheckpointId = None
        self.pos = Point(None, None)
        self.vel = Point(None, None)
        self.boostUsed = False
        self.thrust = 100
    
    def update_values(self):
        lastCheckpoint = self.nextCheckpointId
        x, y, vx, vy, self.angle, self.nextCheckpointId = [int(i) for i in input().split()]
        self.pos = Point(x, y)
        self.vel = Point(vx, vy)
        if lastCheckpoint != self.nextCheckpointId:
            self.totalCheckpoints += 1

    def determine_target(self):
        nextPos = self.pos + self.vel * 3
        if nextPos.distance(checkpoints[self.nextCheckpointId]) < 600:
            self.nextCheckpointId += 1
            if self.nextCheckpointId == checkpointCount:
                self.nextCheckpointId = 0

        self.target = checkpoints[self.nextCheckpointId]

    def set_target(self, target):
        self.target = target

    def polish_target(self):
        print(f"target {self.target}", file=sys.stderr)
        correctur_fac = 0.75
        new_x = self.target.getX()
        new_y = self.target.getY()
        if self.vel.getX() != 0:
            time = (self.target.getX() - self.pos.getX()) / self.vel.getX()
            if time > 0:
                print(f"time ${time}", file=sys.stderr)
                landing_y = self.pos.getY() + time * self.vel.getY()
                new_y = self.target.getY() + (self.target.getY() - landing_y) * correctur_fac
        if self.vel.getY() != 0:
            time = (self.target.getY() - self.pos.getY()) / self.vel.getY()
            if time > 0:
                print(f"time ${time}", file=sys.stderr)
                landing_x = self.pos.getX() + time * self.vel.getX()
                new_x = self.target.getX() + (self.target.getX() - landing_x) * correctur_fac
                
        self.target = Point(new_x, new_y)
        print(f"new target {self.target}", file=sys.stderr)

    def determine_thrust(self, firstRound = False):
        if firstRound and self.pos.distance(self.target) > 4000:
            print(f"first round boost", file=sys.stderr)
            self.thrust = "BOOST"
            return
        if not self.boostUsed and self.pos.distance(self.target) > 8000:
            print(f"normal boost", file=sys.stderr)
            self.thrust = "BOOST"
            return
        if not self.boostUsed and self.totalCheckpoints > checkpointCount and self.pos.distance(self.target) > 4000:
            print(f"second round boost", file=sys.stderr)
            self.thrust = "BOOST"
            return
        self.thrust = 100
    
    def debug(self):
        print(f"angle {self.angle}", file=sys.stderr)
        
    def print_output(self):
        if self.thrust == "BOOST":
            self.boostUsed = True
        print("{0} {1} {2}".format(
            int(self.target.getX()), int(self.target.getY()), self.thrust))

# read static game values
checkpoints = []
laps = int(input())
checkpointCount = int(input())
for _ in range(checkpointCount):
    checkpoints.append(Point(*[int(i) for i in input().split()]))

player1 = Player()
player2 = Player()
opponent1 = Player()
opponent2 = Player()

firstRound = True
# game loop
while True:
    player1.update_values()
    player2.update_values()
    opponent1.update_values()
    opponent2.update_values()

    # determine targets: next checkpoint for player1, first opponent for player2
    player1.determine_target()
    first_opponent = opponent1
    if opponent2.totalCheckpoints > opponent1.totalCheckpoints:
        first_opponent = opponent2
    player2.set_target(first_opponent.pos + first_opponent.vel * 8)

    player1.determine_thrust(firstRound)
    player2.determine_thrust()

    player1.polish_target()
    #player2.polish_target()
    
    player1.debug()

    player1.print_output()
    player2.print_output()

    firstRound = False
    