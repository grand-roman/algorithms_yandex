def make_dict(word):
  result = {}

  for letter in word:
    if(letter in result):
      result[letter] += 1
    else:
      result[letter] = 1

  return result

a = input()
b = input()
print(make_dict(a) == make_dict(b))
