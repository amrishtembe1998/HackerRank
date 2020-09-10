count1 = 0
counter2 = 0
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
for i in range(len(apples)):
    if((a+apples[i])>=s and (a+apples[i])<=t):
        count1 = count1 + 1
for i in range(len(oranges)):
    if((b+oranges[i])>=s and (b+oranges[i])<=t):
        counter2 = counter2 + 1
print(count1,counter2)
