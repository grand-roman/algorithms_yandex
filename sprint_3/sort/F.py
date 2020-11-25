a = int(input())
if a!=0:
  mas = list(map(int, input().split()))
  b1 = []
  b2 = []
  for i in mas:
    if i%2==0:
      b1.append(i)
    else:
      b2.append(i)
  for i in range(len(b1)):
    print(b1[i],end = ' ')
    print(b2[i], end= ' ')
