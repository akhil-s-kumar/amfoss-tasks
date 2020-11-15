n = int(input())
if n>=1 and n<=(10**6):
    a = []
    ainput = input()
    alist = ainput.split()
    for i in alist:
        aele = int(i)
        if aele>=1 and aele<=(10**9):         
            a.append(aele)
        else:
            print("Element size should not exceed!")
            break
    b = []
    binput = input()
    blist = binput.split()
    for j in blist:
        bele = int(j)
        if bele>=1 and bele<=(10**9):         
            b.append(bele)
        else:
            print("Element size should not exceed!")
            break
    c = []
    for k in range(0, n):
        if b[k]//a[k]>=1:
            d = b[k]//a[k]
            c.append(d)
        else:
            print("No death notes can be made")
            
    print(min(c))
