f = open('input.txt', 'r')
a = int(f.readline())
mas = list(map(int, f.readline().rstrip().rsplit()))

def insertSort(array,a):
  for j in range(1, a):
    for i in range(j):
      if array[j] < array[i]:
        intermediate = array[i]
        array[i] = array[j]
        array[j] = intermediate

  return ' '.join(map(str, array))

print(insertSort(mas,a))
