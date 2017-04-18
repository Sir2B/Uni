def is_tidy(number):
    last_c = '0'
    for char in number:
        if char >= last_c:
            last_c = char
            continue
        else:
            return False
    return True

t = int(raw_input())

for i in xrange(1, t + 1):
    n = int(raw_input())
    searching = True
    last_c = '9'
    n = list(str(n))
    index = len(n)-1
    while searching:
        if is_tidy(n):
            print "Case #{}: {}".format(i, int("".join(n)))
            searching = False
        elif n[index] == '9':
            index -= 1
            continue
        else:
            front_char = n[0:index]
            back_char = n[index+1:]
            front_number = int("".join(front_char))
            front_number -= 1
            n = list(str(front_number)) + ['9'] + back_char
            index -= 1
            continue



