def isAvailable(x, y, N):
    return (x>=0 and x<N) and (y>=0 and y<N)

def rectangular_triangle(n):
    a = [[' ']*n for i in range(n)]
    for i in range(n):
        a[n-1][i] = '*'
    for i in range(n):
        a[i][n-1] = '*'
    i = 0
    j = n-1
    while isAvailable(i+1,j-1,n):
        a[i][j] = '*'
        i += 1
        j -= 1
    for i in a:
        print(''.join(i))