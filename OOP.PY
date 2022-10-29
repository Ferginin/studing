n, a, b, c, d = map(int, input().split())
*m, = range(n+1)
m[a:b+1] = m[b:a-1:-1]
m[c:d+1] = m[d:c-1:-1]
print(*m[1:])