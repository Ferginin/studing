def sch(A, x):
    if x in a:
        i = 0
        while A[i] != x and i < len(A)-1:
            i += 1
        left = i
        i = len(A)-1
        while A[i] != x and i != -1:
            i -= 1
        right = i
        if left == right:
            return (right+1)
        else:
            return ((left + right)//2)+1
    else:
        return 0
n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]
for i in b:
    print(sch(a,i), end = ' ')