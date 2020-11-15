n = int(input())
if n>1 and n<30:
    a = []
    if n%2==1:
        for i in range(1,n+1):
            if i%2==0:
                continue
            else:
                a.append(i)
    else:
        print("n is a even number")
    b = a[::-1]
    b.pop(0)
    for j in a:
        c = n-j
        c = c//2
        print("*"*c+"D"*j+"*"*c)
    for k in b:
        d = n-k
        d = d//2
        print("*"*d+"D"*k+"*"*d)
elif n<1:
    print("n should be greater than 1") 
elif n>30:
    print("n should be greater than 30")
