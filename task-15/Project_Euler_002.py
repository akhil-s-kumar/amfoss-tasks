a = [1,2]
for j in range(2,80):
    a.append(a[j-1]+a[j-2])
t = int(input())
for i in range(t):
    n = int(input())
    sumf = 0
    for k in range(len(a)):
        if a[k]%2==0 and a[k]<n:
            sumf +=a[k]
    print(sumf)
