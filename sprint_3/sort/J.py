def sort_count(mas):
  max_max = max(mas)
  mas_count = [0] * (max_max + 1)
  for i in mas:
    mas_count[i]+=1
  '''
  j = 0
  sort_mas = []
  while j!=len(mas_count):
    while mas_count[j]!=0:
      sort_mas.append(j)
      mas_count[j]-=1
    j+=1
  '''
  return mas_count

n=int(input())
mas = [int(i) for i in input().split(' ')]
m=int(input())
if m>0:
  spec_mas = [int(i) for i in input().split(' ')]
res = []
sort_k = sort_count(mas)
for i in range(m):
  while sort_k[spec_mas[i]]!=0:
    res.append(spec_mas[i])
    sort_k[spec_mas[i]]-=1
for i in range(len(sort_k)):
  while sort_k[i]!=0:
    res.append(i)
    sort_k[i]-=1
print(*res)

