n = int(input())
m = int(input())
mat = []
for i in range(n):
  mat.append([i for i in input().split(' ')])
k = 0
l = 0
le = n*m
for v in range(n//2+1):
    #Заполнение верхней горизонтальной матрицы
    for i in range(m-k):
      print(mat[v][i+v])
      l+=1
    if l==le:
      break
    #Заполнение правой вертикальной матрицы
    for i in range(v+1, n-v):
      print(mat[i][-v-1])
      l+=1
    if l==le:
      break
    #Заполнение нижней горизонтальной матрицы
    for i in range(v+1, m-v):
      print(mat[-v-1][-i-1])
      l+=1
    if l==le:
      break

    #Заполнение левой вертикальной матрицы
    for i in range(v+1, n-(v+1)):
      print(mat[-i-1][v])
      l+=1
    if l==le:
      break
    k+=2
