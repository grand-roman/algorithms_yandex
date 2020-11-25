def coeficentes(a, b, c):
  x = 0
  y = 0
  while abs(x * a - y * b) != c:
    if a < b:
      if x * a > y * b:
        y += 1
      else:
        x += 1
    else:
      if x * a < y * b:
        x += 1
      else:
        y += 1
  
  if x * a > y * b:
    return x, -y, c
  else:
    return -x, y, c

a = int(input())
b = int(input())
res = 1
if a==b:
  print(*coeficentes(a,b,a))
else:
  for i in reversed(range(1,(max(a,b)//2)+1)):
    if a%i==0 and b%i==0:
      res = i
      break
  print(*coeficentes(a,b,res))
