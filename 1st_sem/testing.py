a = [1,5,6,7,10]
b = [1,2,5,6,15,22]
res = []
j = 0
print('start')
for i in range(len(a)):
    if len(b) == j:
        break
    if a[i] == b[j]:
        res.append(i+1)
        j += 1
    else:
        while len(b) != j and a[i] > b[j]:
            res.append(0)
            j += 1
            if a[i] == b[j]:
                res.append(i+1)
                j += 1
        if len(b) == j:
            break
while len(b) > j:
    res.append(0)
    j += 1
    
print(*res)