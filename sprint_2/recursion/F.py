a = int(input())
res = 1
while True:
  if a==0:
    break
  else:
    res*=a
    a-=1
print(res)
