t = int(raw_input())

for i in xrange(1, t + 1):
    c = 0
    k, s = raw_input().split(" ")
    s = int(s)
    k = list(k)
    for a in xrange(len(k)-s+1):
        if k[a] == '-':
            c += 1
            for b in xrange(a, a+s):
                k[b] = '+' if k[b] == '-' else '-'
    print "Case #{}: {}".format(i, 'IMPOSSIBLE' if '-' in k else c)

