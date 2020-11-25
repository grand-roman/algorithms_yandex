a = int(input())
b = int(input())
res = 1
if a==b:
  print(a)
else:
  for i in reversed(range(1,max(a,b)//2)):
    if a%i==0 and b%i==0:
      res = i
      break
  print(res)
