# 0 1 3 6 10 15 21 28 36 45
# 2 4 7 11 16 22 29 37 46 55
# 5 8 12 17 23 30 38 47 56 64
# 9 13 18 24 31 39 48 57 65 72
# 14 19 25 32 40 49 58 66 73 79
# 20 26 33 41 50 59 67 74 80 85
# 27 34 42 51 60 68 75 81 86 90
# 35 43 52 61 69 76 82 87 91 94
# 44 53 62 70 77 83 88 92 95 97
# 54 63 71 78 84 89 93 96 98 99

# 10 10

# 0 1 3 6
# 2 4 7 9
# 5 8 10 11

# 3 4

n,m = map(int, input().split())
k = 0
a = [[0]*m for i in range(n)]
def vgrani(x,y):
    return((x > -1) and (x < n) and (y > -1) and (y < m))

def diagonal(x,y,k1):
    x += 1
    y -= 1
    while vgrani(x,y):
        a[x][y] = k1
        k1 += 1
        x += 1
        y -= 1
    return(k1) 

i = 0
j = 0
while k != n * m:
    a[i][j] = k
    k = diagonal(i,j,k+1)
    j += 1
    if not vgrani(i, j):
        i += 1
        j -= 1
for i in range(n):
    print(*a[i])