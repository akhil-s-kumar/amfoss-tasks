t = int(input())
for i in range(t):
    n = []
    ninput = input()
    nstring = ninput.split()
    for j in nstring:
        nconvert = int(j)
        n.append(nconvert)
    k = []
    kinput = input()
    kstring = kinput.split()
    for l in kstring:
        kconvert = int(l)
        k.append(kconvert)
    maxvalue = []
    a  = max(k)
    k.remove(a)
    b = a-n[1]
    c=b
    for m in k:
        c = c*m
    print(c)
