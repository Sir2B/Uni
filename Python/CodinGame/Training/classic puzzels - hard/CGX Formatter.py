from __future__ import print_function
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def split(delimiters, string):
    string = string.strip()
    return string
    
def ident(mystring):
    ident_n = 0
    result = ""
    string_started = False
    is_new_line = False
    for char in mystring:
        if char == "'":
            string_started = not string_started
        if string_started:
            if is_new_line:
                result += ident_n * ' '
                is_new_line = False
            result += char
        else:
            if char == '(':
                if not is_new_line:
                    result += '\n'
                result += " "*ident_n + char + '\n'
                is_new_line = True
                ident_n += 4
            elif char == ')':
                if not is_new_line:
                    result += '\n'
                ident_n -= 4
                is_new_line = False
                result += " "*ident_n + char
            elif char == ';':
                result += char + '\n'
                is_new_line = True
            else:
                if char != " " and char != "\t":
                    if is_new_line:
                        result += ident_n * ' '
                        is_new_line = False
                    result += char
                
                
    return result
        
        

n = int(raw_input())
intend = 0
delimiter = ";()"
mystring = ""
for i in xrange(n):
    cgxline = raw_input()
    mystring += cgxline

mystring = ident(mystring)
#mystring = mystring.replace('\n\n', '\n')
print(mystring.strip())
