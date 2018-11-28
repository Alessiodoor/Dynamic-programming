x = 'acdcfb'
y = 'dacgfb'
n = len(x)
m = len(y)
print("x: " + str(x))
print("y: " + str(y))
c = [[0 for x in range(m)] for y in range(n)]
#CREATE MATRIX OF LENGHTS
tmp = 0
for i in range(n):
    for j in range(m):
        if x[i] != y[j]:
            c[i][j] = 0
        else:
            max = 0
            for s in range(i):
                for t in range(j):
                    if x[s] < x[i] and c[s][t] > max:
                        max = c[s][t]
            c[i][j] = max + 1
        if c[i][j] >= tmp: tmp = c[i][j]
print(tmp)