#https://contest.yandex.ru/contest/18883/run-report/41251384/
'''
- ПРИНЦИП РАБОТЫ -- Задача А-- Нужно определить, какое самое большое число можно из данных чисел составить. Нужно ичпользовать сортировку "алфавитом" но для чисел. Когда мы смотрим на 1 слева разряд больше ли он другого 1 разряда у другого числа, если одинаковый то смотрим на следующий разряд. Алгоритм сортировки использовал quickSort только распределение по сторонам определялось с помощью вспомогательной вункции определения большего числа по "алфавиту"
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Конечно же худшая временная сложность для quickSort это O(n^2). Поэтому проще считать быстродействие использованное на практике это O(nlogn). Что касабельно дополнительной функции она будет константой от которой худший случай это сравнение двух одинаковых чисел с  максимальной длинной. Поэтому средняя сложность O(nlogn)
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Куча памяти, выделенной на сортировку. Массив будет скопирован logn раз O(log2n) O(N^2) в худшем случае и O(NlogN) в среднем.
'''
n = int(input())
mas = input().split(' ')

def check_values(first, second):
  i = j = 0

  while True:
    if first[i] != second[j]:
      return first[i] > second[j]
    i = (i + 1) % len(first)
    j = (j + 1) % len(second)
    if not (i or j):
      return False
  
def quick_sort(array):

  if len(array) < 2:
    return array

  mid = array[0]
  right = []
  left = []

  for item in array[1:]:
    if check_values(item, mid):
      left.append(item)
    else:
      right.append(item)

  return quick_sort(left) + [mid] + quick_sort(right)


result = quick_sort(mas)
print(''.join(result))
