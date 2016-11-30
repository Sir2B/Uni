budget_list = []
people = int(raw_input())
prize = int(raw_input())
for i in xrange(people):
    b = int(raw_input())
    budget_list.append(b)

budget_list.sort()

if sum(budget_list) < prize:
    print "IMPOSSIBLE"
else:
    while (prize > 0):
        average_budget = prize//people
        paying = [b for b in budget_list if b < average_budget]
        for budget in paying:
            budget_list.remove(budget)
            people -= 1
            prize -= budget
            print budget
        if len(paying) == 0:
            budget = min(budget_list)
            budget_list.remove(budget)
            people -= 1
            prize -= average_budget
            print average_budget