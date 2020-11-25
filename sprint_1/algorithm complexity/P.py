tmp = {
    2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'
}
put=input()

result = []

for number in put:

  if not result:
    result = list(map(str, tmp[int(number)]))
    continue
  
  letters = tmp[int(number)]
  inte_result = []

  for letter in result:
    for old_letter in letters:
      inte_result.append(letter + old_letter)

  result = inte_result

print(' '.join(result))
