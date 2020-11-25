def func(mas,rows,columns):
  res = 0
  if rows <= 1:
    return 0
  if columns == 0:
    return 0
  for column in range(columns):
    for row in range(1, rows):
      if mas[row][column] < mas[row - 1][column]:
        res += 1
        break
  return(res)

col = int(input())
leng = int(input())
mas = []
for i in range(col):
  temp = [i for i in input()]
  mas.append(temp)

print(func(mas,col,leng))
