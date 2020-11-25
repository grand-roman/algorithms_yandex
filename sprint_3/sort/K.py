def findNumberOfSlices(array):
  result = 0
  start = 0
  end = 1

  while end < len(array):
    
    if max(array[start:end]) <= min(array[end:]):
      start = end
      end += 1
      result += 1
    else:
      end += 1

  result += 1

  return result

n = int(input())
mas = [int(i) for i in input().split(' ')]
print(findNumberOfSlices(mas))
