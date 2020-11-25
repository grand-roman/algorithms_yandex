def merge_sort(alist, start, end):

    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

def findFlowerbed(array):
  results = []
  intermediate = array[0]

  for i in range(1, len(array)):

    if intermediate[1] >= array[i][0]:
      if intermediate[1] < array[i][1]:
        intermediate[1] = array[i][1]

    else:
      results.append(intermediate)
      intermediate = array[i]

    if i + 1 == len(array):
      results.append(intermediate)

  return results

n=int(input())
mas = []
for i in range(n):
  temp = [int(i) for i in input().split(' ')]
  mas.append(temp)
merge_sort(mas, 0, len(mas))
for i in findFlowerbed(mas):
  print(*i)
