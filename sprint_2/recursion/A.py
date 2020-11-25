def func(i):
  if i==0:
    return 1
  elif i==1:
    return 1
  return func(i-1)+func(i-2)

a = int(input())
print(func(a))
