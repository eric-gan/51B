import random


INSIDE = 3 # change me
CHILDREN = 332 # change me

def get_outside(index):
    return [str(i) for i in range(INSIDE + index*CHILDREN, INSIDE + (index+1)*CHILDREN)]

d = {}

count = 0

for i in range(3):
    a = [str(i), str((i+1) % 3)]
    for k in a:
        if k not in d:
            d[k] = 0
        d[k] += 1 
    print([str(i), str((i+1) % 3)])
    count += 1

for i in range(3):
    for j in range(3):
        count += 1
        a = [str(i)] + (get_outside(j))
        for k in a:
            if k not in d:
                d[k] = 0
            d[k] += 1
        print([str(i)] + (get_outside(j)))
for i in range(3):
    a = [str(i), str(INSIDE + i*CHILDREN)]
    for k in a:
        if k not in d:
            d[k] = 0
        d[k] += 1
    count += 1
    print([str(i), str(INSIDE + i*CHILDREN)])
    a = [str(i), str(INSIDE + (i+1)*CHILDREN - 1)]
    for k in a:
        if k not in d:
            d[k] = 0
        d[k] += 1
    print([str(i), str(INSIDE + (i+1)*CHILDREN - 1)])
for i in range(3):
    a = [str(i)] + get_outside((i + 1) % 3) + get_outside((i + 2) % 3)
    count += 1
    for k in a:
        if k not in d:
            d[k] = 0
        d[k] += 1    
    others = [str(i)] + get_outside((i + 1) % 3) + get_outside((i + 2) % 3)
    print(others)
    for i in range(10):
        count += 1
        random.shuffle(others)
        for k in a:
            if k not in d:
                d[k] = 0
            d[k] += 1   
        print(others)
#print(d)
#print(count)