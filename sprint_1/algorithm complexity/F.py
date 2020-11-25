input()
a = [int(i) for i in input().split(' ')]
b = {}
for i in a:
    if i not in b:
        b[i]= 1
    else:
        b[i]+=1
l = 1
res = a[0]
for k,v in b.items():
    if v>l:
        l=v
        res=k
print(res)
