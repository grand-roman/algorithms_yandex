height = int(input())
col = int(input())
items = []
for i in range(col):
  item = input().split(' ')
  items.append([int(item[0]),int(item[1]),i])
items.sort(key=lambda x: (x[0], -x[1]), reverse=True)
res = []
for i in items:
  if height>=i[1]:
    res.append(i[2])
    height -= i[1]
res.sort()
print(*res)
