a = int(input())
mas = []
for i in range(a):
  temp = input().split(' ')
  t1 = float(temp[0])
  t2 = float(temp[1])
  mas.append([t2,t1])
mas = sorted(mas)
min_begin = mas[0][1]
min_end = mas[0][0]
opt_mas=[[min_begin,min_end]]
length = 1
for i in range(1,a):
  if (mas[i][1]>=min_end):
    min_end = mas[i][0]
    min_begin = mas[i][1]
    opt_mas.append([min_begin,min_end])
    length+=1

print(length)
for i in range(length):
  print(opt_mas[i][0],end = ' ')
  print(opt_mas[i][1])
