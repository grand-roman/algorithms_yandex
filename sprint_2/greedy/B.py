a = int(input())
mas = [int(i) for i in input().split(' ')]
res = 0
for i in range(a-1):
  if mas[i]>mas[i+1]:
    continue
  elif mas[i]<mas[i+1]:
    res+=mas[i+1]-mas[i]
print(res)
