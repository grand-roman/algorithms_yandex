m = int(input())
n = int(input())

matr = []

for i in range(m):
    temp = []
    for j in input().split(' '):
        temp.append(int(j))
    matr.append(temp)

y = int(input())
x = int(input())
temp=[]
if x-1>-1:
    temp.append(matr[y][x-1])
if x+1<n:
    temp.append(matr[y][x+1])
if y-1>-1:
    temp.append(matr[y-1][x])
if y+1<m:
    temp.append(matr[y+1][x])
temp.sort()
print(*temp)
