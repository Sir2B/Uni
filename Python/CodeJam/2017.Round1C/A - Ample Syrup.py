import math

class Pancake(object):
    def __init__(self, radius, height):
        self.height = height
        self.radius = radius
        self.border_area = self.calc_border()
        self.floor_area = self.calc_floor_area()
        self.total_area = self.border_area + self.floor_area

    def calc_area(self):
        return self.calc_border() + self.calc_floor_area()

    def calc_floor_area(self):
        return self.radius*self.radius*math.pi

    def calc_border(self):
        return 2*self.radius*self.height*math.pi

t = int(raw_input())

for test in xrange(1, t + 1):
    total, ordered = [int(i) for i in raw_input().split()]
    pancakes = []


    for a in xrange(total):
        pancakes.append(Pancake(*[int(i) for i in raw_input().split()]))

    max_item = Pancake(0,0)
    max_index = -1
    for index, item in enumerate(pancakes):
        if item.total_area > max_item.total_area:
            max_item = item
            max_index = index

    del pancakes[max_index]
    # for index, item in enumerate(pancakes):
    #     if item.radius < max_item.radius:
    #         del pancakes[index]

    area = 0
    if ordered > 0:
        area += max_item.total_area
        ordered -= 1
    

    pancakes.sort(key=lambda p: p.border_area, reverse=True)
    area += sum([p.border_area for p in pancakes[:ordered]])

    print "Case #{0}: {1:.9f}".format(test, area)

