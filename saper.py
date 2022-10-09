n,m = map(int, input().split())
w = int(input())
a = [[0] * m for i in range(n)]
for i in range(w):
    b,c = map(int, input().split())
    a[b-1][c-1] = '*'
for i in range(n):
    for j in range(m):
        if a[i][j] != '*':
            if j != m-1:
                if (a[i][j+1] == '*'):
                    a[i][j] += 1
            if j != 0:
                if a[i][j-1] == '*':
                    a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] != '*':
            if i != n-1:
                if (a[i+1][j] == '*'):
                    a[i][j] += 1
            if i != 0:    
                if a[i-1][j] == '*':
                    a[i][j] += 1
for i in range(n):
    for j in range(m):
        if (a[i][j] != '*') and (i > 0) and (j > 0) and (i < n-1) and (j < m-1):
            if a[i-1][j-1] == '*':
                a[i][j] += 1
            if a[i-1][j+1] == '*':
                a[i][j] += 1
            if a[i+1][j-1] == '*':
                a[i][j] += 1
            if a[i+1][j+1] == '*':
                a[i][j] += 1
        if (a[i][j] != '*') and (i == 0) and (j > 0) and (j < m-1):
            if a[i+1][j-1] == '*':
                a[i][j] += 1
            if a[i+1][j+1] == '*':
                a[i][j] += 1
        if (a[i][j] != '*') and (i == n-1) and (j > 0) and (j < m-1):
            if a[i-1][j-1] == '*':
                a[i][j] += 1
            if a[i-1][j+1] == '*':
                a[i][j] += 1
        if (a[i][j] != '*') and (j == 0) and (i > 0) and (i < n-1):
            if a[i-1][j+1] == '*':
                a[i][j] += 1
            if a[i+1][j+1] == '*':
                a[i][j] += 1
        if (a[i][j] != '*') and (j == m-1) and (i > 0) and (i < n-1):
            if a[i-1][j-1] == '*':
                a[i][j] += 1
            if a[i+1][j-1] == '*':
                a[i][j] += 1
        if m == 2:
            if i == (n-1) and j == 0:
                if a[i-1][j+1] == '*':
                    a[i][j] += 1
for i in range(n):
    print(*a[i])