def fun(x):
    result = x*(x+1)//2
    return result

t=int(input())
for i in range(t):
    n=int(input())
    n-=1
    a=n//3
    b=n//5
    c=n//15
    print(3*fun(a)+5*fun(b)-15*fun(c))
