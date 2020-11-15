t = int(input())
if t<=20:
    for i in range(1,t+1):
        k1 = int(input())
        a = input()
        words1 = a.split()
        if len(words1)<=200:
            if len(words1)-1>=k1:
                asciisum1 = sum(map(ord,words1[k1]))
                print(asciisum1)
            else:
                asciisum1 = -1
                print(asciisum1)
        else:
            print("The no of words of a setence should be less than or equal to 200")
else:
    print("Enter a number less than or equal to 20")
