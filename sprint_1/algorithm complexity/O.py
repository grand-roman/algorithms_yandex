a = []
for i in input().split(' '):
    if int(i) != 0 :
        a.append(int(i))
input()
input()
for i in input().split(' '):
    a.append(int(i))
a.sort()
print(*a)
