#https://contest.yandex.ru/contest/18997/run-report/42404583/

#Задача A - сколько может быть различных деревьев поиска, содержащих в узлах числа от 1 до n
#Решение простое - Catalan number - https://en.wikipedia.org/wiki/Catalan_number

#-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# ((2n)!) / ((n+1)! * n!) -> O(1) (P.S. с факториалом я запуталя но вопрос не будет ли это выполняться за O(n) ? Мы же все таки вызываем функцию нахождения фактоиала)
#
#
#-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(1)   (P.S. когда писал объяснение думал об одном - писал другое :) )



import math

n = int(input())


def solution(number):
    return int((math.factorial(2 * number)) / ((math.factorial(number + 1)) * (math.factorial(number))))


print(solution(n))

