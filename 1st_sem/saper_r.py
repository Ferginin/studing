n,m = map(int, input().split())
w = int(input())
a = [[0] * m for i in range(n)]

def ifAvailable(x, y):
    return (x>=0 and x<n) and (y>=0 and y<m)

def printCoordinates():
    x, y = map(int, input().split())
    if not ifAvailable(x, y):
        print('Error: Out of range, enter other coordinates.')
        x, y = printCoordinates()
    if a[x][y] == '*':
        print('Error: There is already a mine here, enter other coordinates.')
        x, y = printCoordinates()
    return x, y
    
for i in range(w):
    first, second = printCoordinates()
    a[first][second] = '*'
    for row in range(3):
        for column in range(3):
            x = first-1+row
            y = second-1+column
            if ifAvailable(x, y) and a[x][y] != '*':
                a[x][y] += 1

print("__"*m + "\nResult:")
for i in range(n):
    print(*a[i])