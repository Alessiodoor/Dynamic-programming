import sys

def print_opt(i, c):
    if c <= 0:
        return
    if (opt[i-1][c-(objs[i-1][0])] + objs[i-1][1]) >= opt[i-1][c]:
        print(objs[i - 1])
        print_opt(i - 1, c - (objs[i-1][0]))
    else:
        print_opt(i - 1, c)

#(peso, valore)
if len(sys.argv) <= 1:
    print("Insert parameters")
    sys.exit()
objs = [(1, 1), (2, 6), (5, 18), (6, 22), (7, 28)]
C = int(sys.argv[1]) + 1
n = len(objs) + 1
opt = [[0 for x in range(C)] for y in range(n)]
for i in range(n):
    opt[i][0] = 0

for i in range(1, C):
    opt[0][i] = 0

for i in range(1, n):
    for c in range(1, C):
        if objs[i-1][0] > c:
            opt[i][c] = opt[i-1][c]
        else:
            opt[i][c] = max(opt[i-1][c], (opt[i-1][c-(objs[i-1][0])] +objs[i-1][1]))
#ORIGINL OBJECT
print(objs)
#BAG OBJECTS
print("Bag: ")
print_opt(n - 1, C - 1)