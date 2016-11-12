import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def solu1():
    n = int(raw_input())
    storage = 0
    numbers = []
    for i in xrange(n):
        telephone = raw_input()
        new_length = len(telephone)
        max_existing_numbers = 0
        for number in numbers:
            existing_numbers = 0
            for i in xrange(new_length+1):
                if number.startswith(telephone[:i]):
                    existing_numbers = i
            if existing_numbers > max_existing_numbers:
                max_existing_numbers = existing_numbers
        storage += new_length - max_existing_numbers
        numbers.append(telephone)
    
    print storage

def solu2():
    n = int(raw_input())
    storage = 0
    telephone_dict = {}
    for i in xrange(n):
        local_dict = telephone_dict
        telephone = raw_input()
        for char in telephone:
            if not char in local_dict:
                local_dict[char] = {}
                storage += 1
            local_dict = local_dict[char]
    print storage

solu2()