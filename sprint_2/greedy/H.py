a = int(input())
mas = [int(i) for i in input().split(' ')]
k = 1
elem = []
for i in range(1,a):
  if mas[i]>mas[i-1]:
    k+=1
  else:
    elem.append(k)
    k=1
elem.append(k)
print(max(elem))
