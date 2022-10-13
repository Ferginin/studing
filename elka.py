def spruce(N):
    a = [['.']*((N*2)-1) for i in range(N)]
    j = N-1
    j1 = N-1
    for g in range(N):
        for i in range(g,N):
            a[i][j] = '*'
            a[i][j1] = '*'
        if j != 0:
            j -= 1
            j1 += 1
    for i in a:
        print(''.join(i))