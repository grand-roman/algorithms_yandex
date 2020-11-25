a = int(input())
mas = [int(i) for i in input().split(' ')]
for j in range(a-1):
  for i in range(a-j-1):
    if mas[i]>mas[i+1]:
      mas[i], mas[i+1] = mas[i+1], mas[i]
print(*mas)
