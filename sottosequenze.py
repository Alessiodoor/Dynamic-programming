import sys

def sottosequenza(x):
    l = []
    s = []
    aus = 0
    l.append(1)
    s.append(-1)
    max_tot = 1
    for j in range(1, len(x)):
        max = 0
        for k in range(0, j):
            if x[k] <= x[j] and l[k] > max:
                max = l[k]
                aus = k
        l.append(max+1)
        s.append(aus)
        if l[j] > max_tot: max_tot = l[j]
    return create_list(x, s, max_tot)

def create_list(x, s, lenght):
    max_ind = 0
    max = 0
    for i in range(len(s)):
        if s[i] > max:
            max = s[i]
            max_ind = i
    r = [0] * lenght
    ix = max_ind
    for i in range(lenght, 0, -1):
        r[i-1] = x[ix]
        ix = s[ix]
    return r

print(sottosequenza(list(sys.argv[1].split())))