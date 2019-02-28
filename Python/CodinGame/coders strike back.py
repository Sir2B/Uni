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

    def __mul__(self, other):
        if isinstance(other, Point):
            # scalar product
            return self.getX() * other.getX() + self.getY() * other.getY()
        if isinstance(other, int) or isinstance(other, float):
            return Point(self.getX() * other, self.getY() * other)

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

    def angle(self):
        return (90 - math.degrees(math.atan2(self.getX(), self.getY()))) % 360

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
        self.nextCheckpointIdBlocker = 0
    
    def update_values(self):
        lastCheckpoint = self.nextCheckpointId
        x, y, vx, vy, self.angle, self.nextCheckpointId = [int(i) for i in input().split()]
        self.pos = Point(x, y)
        self.vel = Point(vx, vy)
        if lastCheckpoint != self.nextCheckpointId:
            self.totalCheckpoints += 1

    def determine_target(self):
        # nextPos = self.pos + self.vel * 2.5
        # if nextPos.distance(checkpoints[self.nextCheckpointId]) < 600:
        self.thrust = 100
        for point in range(35):
            if (self.pos + self.vel * point * 0.1).distance(checkpoints[self.nextCheckpointId]) < 600:
                self.thrust = "GLIDE"
                self.nextCheckpointId += 1
                if self.nextCheckpointId == checkpointCount:
                    self.nextCheckpointId = 0
                break

        self.target = checkpoints[self.nextCheckpointId]
        
    def determine_target_blocker(self):
        if self.pos.distance(checkpoints[self.nextCheckpointIdBlocker]) < 600:
            self.nextCheckpointIdBlocker = (self.nextCheckpointIdBlocker - 1) % checkpointCount
        self.target = checkpoints[self.nextCheckpointIdBlocker]

    def set_target(self, target):
        self.target = target

    def polish_target(self):
        print(f"target {self.target}", file=sys.stderr)
        if self.thrust == "GLIDE":
            return
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

        desired_angle = (self.target - self.pos).angle()
        diff_angle = abs(desired_angle - self.angle)
        min_angle = min(360 - diff_angle, diff_angle)
        print(f"min_angle {min_angle}", file=sys.stderr)

        if min_angle < 45:
            self.thrust = 100
        elif min_angle < 90:
            self.thrust = 60
        elif min_angle < 135:
            self.thrust = 30
        else:
            self.thrust = 3
        
    def debug(self):
        print(f"angle {self.angle}", file=sys.stderr)
        print(f"pos {self.pos}", file=sys.stderr)
        print(f"vel {self.vel}", file=sys.stderr)
        
    def print_output(self):
        if self.thrust == "BOOST":
            self.boostUsed = True
        print("{0} {1} {2}".format(
            int(self.target.getX()), int(self.target.getY()), self.thrust))

def collide_in_x_rounds(player1, player2, rounds):
    for round_idx in range(rounds):
        next_pos_1 = player1.pos + player1.vel * round_idx
        next_pos_2 = player2.pos + player2.vel * round_idx
        if next_pos_1.distance(next_pos_2) < 1000:
            return True
    return False

def calculate_evasive_manoeuvre(player):
    return Point(player.pos.getY(), -player.pos.getX())

def check_who_is_first_player(player1, player2):
    if player1.totalCheckpoints > player2.totalCheckpoints:
        return player1
    if player2.totalCheckpoints > player1.totalCheckpoints:
        return player2
    
    dist1 = player1.pos.distance(checkpoints[player1.nextCheckpointId])
    dist2 = player2.pos.distance(checkpoints[player2.nextCheckpointId])
    if dist1 < dist2:
        return player1
    return player2

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
    # player2.determine_target_blocker()
    first_opponent = check_who_is_first_player(opponent1, opponent2)
    # if (player2.pos.distance(first_opponent.pos) < 2000):
    player2.set_target(checkpoints[first_opponent.nextCheckpointId])
    if collide_in_x_rounds(player1, player2, 4):
        print('Collide!!', file=sys.stderr)
        player2.set_target(calculate_evasive_manoeuvre(player2))

    player1.determine_thrust(firstRound)
    player2.determine_thrust()

    if collide_in_x_rounds(player2, first_opponent, 1):
        player2.thrust = 'SHIELD'

    player1.polish_target()
    #player2.polish_target()
    
    player1.debug()

    player1.print_output()
    player2.print_output()

    firstRound = False
    