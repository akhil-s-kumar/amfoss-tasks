def prime(p):
    if p==2:
        return True
    elif p%2 == 0:
        return False
    k = 3
    while k**2<=p:
        if p%k==0:
            return False
        k+=2
    return True

t = int(input())
for j in range(t):
    n = int(input())
    maxp = 0
    for k in range(1,n+1):
        if n%k==0:
            if prime(n//k):
                print(n//k)
                break
