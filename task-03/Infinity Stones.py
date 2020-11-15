t = int(input())
for o in range(0,t):
    n_m_p = []
    n = input()
    a = n.split()
    for i in a:
        b = int(i)
        n_m_p.append(b)
    current_i_s = []
    c = input()
    d = c.split()
    for j in d:
        e = int(j)
        current_i_s.append(e)
    total_i_s = []
    f = input()
    g = f.split()
    for k in g:
        h = int(k)
        total_i_s.append(h)
    total_i_s.sort(reverse=True)
    totalcapacity_i_s = 0
    if len(total_i_s)<n_m_p[2]:
        for l in range(0,len(total_i_s)):
            totalcapacity_i_s = totalcapacity_i_s + total_i_s[l]
    else:
        for l in range(0,n_m_p[2]):
            totalcapacity_i_s = totalcapacity_i_s + total_i_s[l]
    currenttotal_i_s = 0
    for m in range(0,len(current_i_s)):
        currenttotal_i_s = currenttotal_i_s + current_i_s[m]
    if currenttotal_i_s<=totalcapacity_i_s:
        print("YES")
    elif currenttotal_i_s>totalcapacity_i_s:
        print("NO")
