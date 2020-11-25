def findMaxSubstring(array, string):
  resultString = ''
  resultLen = 0

  for word in array:
    pivot = 0

    for letter in string:
      if letter == word[pivot]:
        pivot += 1
      
      if pivot == len(word):
        if len(word) > resultLen:
          resultLen = len(word)
          resultString = word
          break
        elif len(word) == resultLen:
          if word < resultString:
            resultString = word
            break
        break

  return resultString


f = open('input.txt', 'r')

mas = f.readline().strip()
n = int(f.readline())
spec = []

spec = [line.strip() for line in f.readlines() if line.strip()]
f.close()
print(findMaxSubstring(spec,mas))
