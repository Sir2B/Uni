import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

class Game(object):
    def __init__(self):
        self.magic_power = 0
        self.map_size = Position(16001, 7501)
        self.max_thrust = 150
        self.max_power = 500
        self.own_goal = Position(0, 3750)
        self.enemy_goal = Position(16000, 3750)


    def throw(self, wizard, position):
        print "THROW {0} {1} 500".format(position.x, position.y)

    def move(self, wizard, position):
        dist = abs(wizard.position - position)
        thrust = min(self.max_thrust, self.max_thrust*dist/2000)
        print "MOVE {0} {1} 150".format(position.x, position.y)

    def obliviate(self, bludger):
        print "OBLIVIATE {0}".format(bludger.id_)
        self.magic_power -= 5

class Entity(object):
    def __init__(self, e_id, e_type, position, vx, vy, state):
        self.id_ = e_id
        self.type = e_type
        self.position = position
        self.vx = vx
        self.vy = vy
        self.has_snaffel = state
        self.job = "player"



class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def calc_next_entity(self, entities):
        next_entity = None
        next_dist = sys.maxint
        for entity in entities:
            dist = abs(self - entity.position)
            if dist < next_dist:
                next_dist = dist
                next_entity = entity
        return next_entity


game = Game()

my_team_id = int(raw_input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left

if my_team_id == 1:
    game.own_goal, game.enemy_goal = game.enemy_goal, game.own_goal

# game loop
while True:
    game.magic_power += 1
    entities = int(raw_input())  # number of entities still in game
    wizards = []
    enemies = []
    snaffels = []
    bludgers = []
    for i in xrange(entities):
        # entity_id: entity identifier
        # entity_type: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        # x: position
        # y: position
        # vx: velocity
        # vy: velocity
        # state: 1 if the wizard is holding a Snaffle, 0 otherwise
        entity_id, entity_type, x, y, vx, vy, state = raw_input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)
        entity = Entity(entity_id, entity_id, Position(x, y), vx, vy, state)
        if entity_type == "WIZARD":
            wizards.append(entity)
        elif entity_type == "OPPONENT_WIZARD":
            enemies.append(entity)
        elif entity_type == "SNAFFLE":
            snaffels.append(entity)
        elif entity_type == "BLUDGER":
            bludgers.append(entity)
        else:
            pass

    diff_to_goal = sys.maxint
    goalkeeper = None
    for wizard in wizards:
        diff = abs(wizard.position - game.own_goal)
        if diff < diff_to_goal:
            diff_to_goal = diff
            goalkeeper = wizard
    goalkeeper.job = "goalkeeper"

    for wizard in wizards:
        next_bludger = wizard.position.calc_next_entity(bludgers)
        if abs(next_bludger.position - wizard.position) < 2000 and game.magic_power > 5:
            print >> sys.stderr, next_bludger.vx
            game.obliviate(next_bludger)
            continue
        if wizard.job == "goalkeeper":
            if wizard.has_snaffel:
                game.throw(wizard, game.enemy_goal)
            else:
                next_snaffel = game.own_goal.calc_next_entity(snaffels)
                move_pos = next_snaffel.position
                # next_enemy = wizard.position.calc_next_entity([e for e in enemies if e.has_snaffel])
                # if next_enemy:
                #     move_pos = next_enemy.position
                # else:
                #     move_pos = Position(abs(game.own_goal.x-650), game.own_goal.y)
                game.move(wizard, move_pos)
            continue

        if wizard.has_snaffel:
            game.throw(wizard, game.enemy_goal)
        else:
            next_snaffel = wizard.position.calc_next_entity(snaffels)
            game.move(wizard, next_snaffel.position)

    # for i in xrange(2):

    #     # Write an action using print
    #     # To debug: print >> sys.stderr, "Debug messages..."


    #     # Edit this line to indicate the action for each wizard (0 <= thrust <= 150, 0 <= power <= 500)
    #     # i.e.: "MOVE x y thrust" or "THROW x y power"
    #     print "MOVE 8000 3750 100"
