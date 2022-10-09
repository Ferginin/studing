mx = -1
a = [i for i in input().split()]
a1 = [0]*len(a)
b = set()
for i in range(len(a)):
    b.add(a[i])
i = 0
for j in b:    
    if a.count(j) > mx:
        mx = a.count(j)
    a1[i] = a.count(j)
    i += 1
h = a1.index(mx)
a2 = a1[::-1]
h1 = a2.index(mx)
print(h,h1)
if h == h1:
    print(b[h])
else:
    if b[h] < b[h1]:
        print(b[h])
    elif b[h] > b[h1]:
        print(b[h1])
