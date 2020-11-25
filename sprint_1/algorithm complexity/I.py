first = input()[::-1]
second = input()[::-1]

diff = len(first) - len(second)

if(diff < 0):
  first += '0'*(abs(diff))
elif(diff > 0):
  second += '0'*(diff)

result = []
counter = 0

for i in range(len(first)):
  if(int(first[i]) == 0):
    if(int(second[i]) == 0):
      if(counter == 1):
        result.append(1)
      else:
        result.append(0)
      counter = 0
    else:
      if(counter == 1):
        result.append(0)
      else:
        result.append(1)
  else:
    if(int(second[i]) == 0):
      if(counter == 1):
        result.append(0)
      else:
        result.append(1)
    else:
      if(counter == 1):
        result.append(1)
      else:
        result.append(0)
        counter = 1

if(counter != 0):
  result.append(1)
print(''.join(str(item) for item in result)[::-1])
