put = input().split(' ')
k = int(input())
res = {}
for i in put:
    res[i]=res[i]+1 if i in res else 1
put=[]
for i in range(k):
    maxi=0
    m=0
    for j in res.items():
        if j[1]>maxi and j[0] not in put:
            maxi=j[1]
            m=j[0]
    put.append(m)
    print(m, end=' ')

