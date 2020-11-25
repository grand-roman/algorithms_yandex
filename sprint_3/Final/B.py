#https://contest.yandex.ru/contest/18883/run-report/41249505/
'''
- ПРИНЦИП РАБОТЫ -- Задача B--
Нужно отсортировать полученные значения из 2 списков, Соединять массивы нельзя. После сортировки нужно определить такое значение "треш-индекса", что половина населенных пунктов имеют значение индекса не меньше его, а половина - не больше.Если количество населенных пунктов четное, то среднее значение нужно считать, как полусумму двух центральных элементов.
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(log(m + n))
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
дополниетльных списков нет, константы не считаем значит O(1)
--P.S Большое спасибо за видео - очень круто прям было))
'''
def find_median_sorted_arrays(mas1, mas2):
    if (len(mas1) > len(mas2)):
        return find_median_sorted_arrays(mas2, mas1);
    x = len(mas1)
    y = len(mas2)
    low = 0
    high = x
    while low <= high:
        partitionX = (low + high)//2
        partitionY = (x + y + 1)//2 - partitionX
        if (partitionX == 0):
            maxLeftX = float("-inf")
        else:
            maxLeftX = mas1[partitionX - 1]
        if (partitionX == x):
            minRightX = float("inf")
        else:
            minRightX = mas1[partitionX];
        if (partitionY == 0):
            maxLeftY = float("-inf")
        else:
            maxLeftY = mas2[partitionY - 1]
        if (partitionY == y):
            minRightY = float("inf")
        else:
            minRightY = mas2[partitionY]
        if (maxLeftX <= minRightY and maxLeftY <= minRightX):
            if ((x + y) % 2 == 0):
                return ((max(maxLeftX, maxLeftY) + min(minRightX, minRightY)))/2
            else:
                return max(maxLeftX, maxLeftY)
        elif (maxLeftX > minRightY):
            high = partitionX - 1;
        else:
            low = partitionX + 1;

n = int(input())
m = int(input())
array_1 = [int(i) for i in input().split(' ')]
array_2 = [int(i) for i in input().split(' ')]

print(find_median_sorted_arrays(array_1, array_2))
