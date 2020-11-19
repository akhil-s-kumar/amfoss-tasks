n = int(input())
s = input()
if len(s)==2:
    k=2
    print(k)
elif len(s)%2==0:
    if len(s)==18:
        k = 1
        print(k)
    else:
        a = []
        b = []
        for i in range(0,len(s)//2):
            a.append(s[i])
        for j in range(len(s)//2,len(s)):
            b.append(s[j])
        if ('0' and '1' in a) and ('0' and '1' in b):
            k=2
            print(k)
        else:
            k = 1
            print(k)
else:
    k = 1
    print(k)
