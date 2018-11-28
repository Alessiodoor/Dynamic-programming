x = 'acdcab'
y = 'dfcgab'
n = len(x) + 1
m = len(y) + 1
print("x: " + str(x))
print("y: " + str(y))
c = [[0 for x in range(m)] for y in range(n)]
#CREATE MATRIX OF LENGHTS
for i in range(1, n):
    for j in range(1, m):
        if x[i - 1] == y[j - 1]:
            c[i][j] = 1 + c[i - 1][j - 1]
        else:
            c[i][j] = max(c[i][j - 1], c[i - 1][j])
#CREATE LIST OF COMMON SEQUENCE
i = n - 1
j = m - 1
r = ''
while i > 0 and j > 0:
    if x[i - 1] == y[j - 1]:
        r = x[i - 1] + r
        i -= 1
        j -= 1
    else:
        if c[i][j - 1] > c[i - 1][j]:
            j -= 1
        else:
            i -= 1
print("Common sequence: " + str(r))