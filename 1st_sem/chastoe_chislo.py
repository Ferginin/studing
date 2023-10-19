mx = -1
a = [i for i in input().split()]
a.sort()
sl = {}
for i in range(len(a)):
    if a[i] in sl:
        sl[a[i]] += 1
    else:
        sl[a[i]] = 1
for word in sl:  
    if sl[word] > mx:
        mx = sl[word]
        res = word
print(res)