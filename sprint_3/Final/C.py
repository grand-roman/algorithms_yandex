#https://contest.yandex.ru/contest/18883/run-report/41252696/
'''
- ПРИНЦИП РАБОТЫ -- Задача С-- Нужно реализовать Поразрядную сортировку
В чем смысл сортировки radix. Мы смотрим на разряды и сортируем по ним учитывая Устойчивость предыдущей сортировки по предыдущему разряду.
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Зависит от k - количество разрядов в самом длинном ключе, но поскольку это будет считаться константой, а мы их не считаем то Сложность алгоритма O(n).
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дополнительный список array и промежуточный список interm_array
пространственная сложность - O(n)
'''
n = int(input())
mas = input().split()

def radix_sort(array, k=6):

  for j in range(k-1, -1, -1):
    interm_array = [[] for i in range(10)]

    for item in array:
      if len(item) != k:
        index = j - k + len(item)
        if 0 <= index < len(item):
          interm_array[int(item[index])].append(item)
        else:
          interm_array[0].append(item)
      else:
        interm_array[int(item[j])].append(item)
    array = []
    for item in interm_array:
      array += item

  return array

print(' '.join(radix_sort(mas)))
