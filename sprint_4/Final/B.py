#https://contest.yandex.ru/contest/18997/run-report/42442229/

#Задача B - найти максимальный путь в дереве. Путь не обязательно должен проходить через корень или содержать лист. Решение такое ходим по веткам и собираем все возможные суммы и после находим максимальное.
#-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(n) - так как вызывается n-1 раз
#-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(1) (считал что O(n) потому что используется список (results) внутри функции, но я сейчас подумал и там не O(n))



class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(node):
    max_result = float('-inf')
    
    def find_branch_max(current):
        nonlocal max_result
        results = [current.value]
        left_max = 0
        right_max = 0
    
        if current.left is not None:
            left_max = find_branch_max(current.left)
            results.append(left_max + current.value)
    
        if current.right is not None:
            right_max = find_branch_max(current.right)
            results.append(right_max + current.value)

        branch_max = max(results)
        
        node_max = max(left_max + current.value + right_max, branch_max)
        if node_max > max_result:
            max_result = node_max

        return branch_max
    
    
    find_branch_max(node)

    return max_result

