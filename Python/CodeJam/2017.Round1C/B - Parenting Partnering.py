class Activity(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.time = end-start

t = 1# int(raw_input())

def have_you_an_activity(camerons_a, start, end):
    for a in camerons_a:
        if start < a.start < end:
            return True
    return False

for test in xrange(1, t + 1):
    cameron, jamie = 0, 0 #[int(i) for i in raw_input().split()]
    
    camerons_a = []
    jamies_a = []
    jamies_time = 720*2
    camerons_time = 0
    exchanges = 0

    for a in xrange(cameron):
        camerons_a.append(Activity(*[int(i) for i in raw_input().split()]))
    for a in xrange(cameron):
        jamies_a.append(Activity(*[int(i) for i in raw_input().split()]))

    camerons_a.append(Activity(540,600))
    jamies_a.append(Activity(840,900))

    for a in jamies_a:
        jamies_time -= a.time
        camerons_time += a.time
        exchanges += 2

    for i in xrange(len(jamies_a)-1):
                start = jamies_a[i].end
                end = jamies_a[i+1].start
                if not have_you_an_activity(camerons_a, start, end):
                    exchanges -= 2
                    jamies_time -= end-start
                    camerons_time += end-start

    for i in xrange(len(camerons_a)-1):
            start = camerons_a[i].end
            end = camerons_a[i+1].start
            if not have_you_an_activity(jamies_a, start, end):
                exchanges -= 2
                camerons_time -= end-start
                jamies_time += end-start
    
    start_a_jam = min([x.start for x in jamies_a])
    start_a_cam = min([x.start for x in camerons_a])
    if start_a_cam > start_a_jam:
        camerons_time += start_a_jam
        jamies_time -= start_a_jam
        exchanges -= 1

    end_a_jam = max([x.end for x in jamies_a])
    end_a_cam = max([x.end for x in camerons_a])
    if end_a_jam > end_a_cam:
        camerons_time += (1440-end_a_jam)
        jamies_time -= (1440-end_a_jam)
        exchanges -= 1

    if jamies_time != 720:
        exchanges += 1
        


    print "Case #{0}: {1:.9f}".format(test, exchanges)

