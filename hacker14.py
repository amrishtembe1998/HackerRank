n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
counter = 0

if(m==1):
    for i in range(0,(len(s)-m)):
        if(s[i]==d):
            counter = counter + 1
elif(m==2):
    for i in range(len(s)-(m-(m-1))):
        if(s[i]+s[i+1]==d):
            counter += 1
elif(m==3):
    for i in range(len(s)-(m-(m-1))):
        if(s[i]+s[i+1]+s[i+2]==d):
            counter += 1

print(counter)
            

