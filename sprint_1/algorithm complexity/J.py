def make_dict(word):
  result = {}

  for letter in word:
    if(letter in result):
      result[letter] += 1
    else:
      result[letter] = 1

  return result

def findnot2(x):
    for k,v in x.items():
        if v!=2:
            return k

input()
a = input().split(' ')
print(findnot2(make_dict(a)))
