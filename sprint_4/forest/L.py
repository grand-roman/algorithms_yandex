import heapq
from collections import deque

k = int(input())

def solution(k):
  array = [1,2,3,5]

  if k < 6:
    return k

  queue_1 = deque()
  queue_2 = deque([[2,2], [3,3], [5,5]])


  while True:

    while queue_2:
      item = queue_2.popleft()

      if item[1] == 2:
        for i in [2,3,5]:
          queue_1.append([item[0] * i, i])
          array.append(item[0] * i)
      elif item[1] == 3:
        for i in [3,5]:
          queue_1.append([item[0] * i, i])
          array.append(item[0] * i)
      else:
        queue_1.append([item[0] * 5, 5])
        array.append(item[0] * 5)

    if len(array) - 1 >= k:
      queue_life = queue_1
      break

    while queue_1:
      item = queue_1.popleft()

      if item[1] == 2:
        for i in [2,3,5]:
          queue_2.append([item[0] * i, i])
          array.append(item[0] * i)
      elif item[1] == 3:
        for i in [3,5]:
          queue_2.append([item[0] * i, i])
          array.append(item[0] * i)
      else:
        queue_2.append([item[0] * 5, 5])
        array.append(item[0] * 5)

    if len(array) - 1 >= k:
      queue_life = queue_2
      break

  while len(array) != k:
    heapq._heapify_max(array)
    array.pop(0)

  heapq._heapify_max(array)

  while queue_life:
    item = queue_life.popleft()

    if item[1] == 2:
      for i in [2,3,5]:
        if item[0] * i < array[0]:
          array[0] = item[0] * i
          queue_life.append([item[0] * i, i])
          heapq._heapify_max(array)

    if item[1] == 3:
      for i in [3,5]:
        if item[0] * i < array[0]:
          array[0] = item[0] * i
          queue_life.append([item[0] * i, i])
          heapq._heapify_max(array)

    if item[1] == 5:
      if item[0] * 5 < array[0]:
        array[0] = item[0] * 5
        queue_life.append([item[0] * 5, 5])
        heapq._heapify_max(array)

  return array[0]

print(solution(k))
