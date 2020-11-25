#https://contest.yandex.ru/contest/18285/run-report/38072389/

def find_col_photo(col_data,weight_photo):
  result = 0
  weight_photo = sorted(weight_photo, reverse=True)
  
  if col_data < 2:
    return 0
  while True:
    weight_photo[0] -= 1
    weight_photo[1] -= 1

    if -1 == weight_photo[0] or -1 == weight_photo[1]:
      return 0

    result += 1
    weight_photo = sorted(weight_photo, reverse=True)
    
    if weight_photo[0] == 0 or weight_photo[1] == 0:
      break

  return result

col_data = int(input())
weight_photo = [int(i) for i in input().split(' ')]
res = find_col_photo(col_data,weight_photo)
print(res)
