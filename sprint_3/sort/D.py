def quicksort(array):
  if len (array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

def findNumberInArray(array, n):
  if len(array) == 0:
    return False
  if len(array) == 1:
    if array[0] == n:
      return True
    else:
      return False
  if array[int(len(array) / 2)] == n:
    return True
  elif array[int(len(array) / 2)] > n:
    return findNumberInArray(array[:int(len(array) / 2)], n)
  else:
    return findNumberInArray(array[int(len(array) / 2):], n)
def findNumberInArrayN(array, n):
  for item in array:
    if item == n:
      return True
  return False

a1 = int(input())
a2 = int(input())
if a1 == 0 or a2 == 0:
  print()
else:
  mas1 = list(map(int, input().split(' ')))
  mas2 = list(map(int, input().split(' ')))
  mas2 = quicksort(mas2)
  res = []
  for i in mas1:
    if findNumberInArray(mas2, i):
      if findNumberInArrayN(res, i):
        continue
      mas2.remove(i)
      res.append(i)
  print(*res)
