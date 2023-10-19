# n = int(input())
# a = [int(i) for i in input().split()]
# m = int(input())
# b = [int(i) for i in input().split()]
a = [1,5,6,7,10]
b = [1,2,5,6,15,22]
res = []
i = 0
j = 0
while j <= len(a)-1 and i <= len(b)-1:
    if b[i] == a[j]:
        res.append(j+1)
        j += 1
        i += 1
    elif b[i] > a[j]: 
        j += 1
    elif b[i] < a[j]:
        res.append(0)
        i += 1
print(*res)