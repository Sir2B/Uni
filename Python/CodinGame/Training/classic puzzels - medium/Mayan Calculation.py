from collections import defaultdict
import sys
import math

dictionary = defaultdict(list)
length, height = [int(i) for i in raw_input().split()]
for i in xrange(height):
    numeral = raw_input()
    for num, line in enumerate([numeral[i:i+length] for i in range(0, len(numeral), length)]):
        dictionary[num].append(line)
        
def find_key(value):
    for k, v in dictionary.items():
        if v == value:
            return k
        
print >> sys.stderr, dictionary
num1 = num2 = 0
s1 = int(raw_input())
exp1 = s1//height-1
for exp in xrange(exp1,-1,-1):
    may_num = []
    for i in xrange(height):
        num_1line = raw_input()
        may_num.append(num_1line)
    num = find_key(may_num)
    num1 += int(num * math.pow(20,exp))

s2 = int(raw_input())
exp2 = s2//height-1
for exp in xrange(exp2,-1,-1):
    may_num = []
    for i in xrange(height):
        num_2line = raw_input()
        may_num.append(num_2line)
    num = find_key(may_num)
    num2 += int(num * math.pow(20,exp))
    
operation = raw_input()


if operation == "+":
    result = num1+num2
elif operation == "-":
    result = num1-num2
elif operation == "*":
    result = num1*num2
elif operation == "/":
    result = num1/num2
    
print >> sys.stderr, "{0} {1} {2} = {3}".format(num1, operation, num2, result)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
if result == 0:
    for l in dictionary[0]:
        print l
big_exp = int(math.log(result)/math.log(20))
for exp in range(big_exp, -1, -1):
    num = result//int(math.pow(20, exp))
    may_num = dictionary[num]
    for l in may_num:
        print l
    result -= num*int(math.pow(20, exp))
    