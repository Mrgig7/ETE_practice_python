list = [int(i) for i in input().split(' ')]
d = {}
d['2'] = 0
d['3'] = 0
d['5'] = 0
for i in list:
    if i % 2 == 0:
        d['2'] += 1
    if i % 3 == 0:
        d['3'] += 1
    if i % 5 == 0:
        d['5'] += 1

print(d)