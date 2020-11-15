t = int(input())
if t>=1 and t<=1000:
    series = []
    for i in range(0,1000000):
        if i==0:
            continue
        elif i==1:
            series.append(i)
        elif i==2:
            series.append(i)
        elif i==3:
            series.append(i)
        else:
            a = (series[i-2]+series[i-3]+series[i-4])%(10**9+7)
            series.append(a)
    for j in range(1,t+1):
        n = int(input())
        if n>=1 and n<=1000000:
            b = series[n-1]
            c = str(b)
            d = []
            for k in c:
                d.insert(0,k)
            separator = ''
            e = int(separator.join(d))
            print(e)
        else:
            print("n should be between 1 and 1000000")
