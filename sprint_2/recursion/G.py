def func(x):
  if ord(x)==97:
    return 'a'
  y = chr(ord(x)-1)
  return func(y)+' '+x

a = input()
print(func(a))
