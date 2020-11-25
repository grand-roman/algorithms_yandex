class StackKeepSum:
  def __init__(self):
    self.list = []
    self.sum = 0
  def push(self, value):
    self.list.append(value)
    self.sum += value[1]
  def pop(self):
    result = self.list.pop()
    self.sum -= result[1]
    return result
  def get_sum(self):
    return self.sum
  def to_tuple(self):
    copied = self.list.copy()
    copied.sort()
    return tuple(copied)

def solution(m, answer, temp_stack):
  collected_amount = temp_stack.get_sum()
  if collected_amount == m:
    answer.add(temp_stack.to_tuple())
    return
  elif collected_amount > m:
    return
  for index, coin in enumerate(coins):
    temp_stack.push((index, coin))
    solution(m, answer, temp_stack)
    temp_stack.pop()

amount = int(input())
input()
coins = [int(x) for x in input().split(" ")]
variants = set()
solution(amount, variants, StackKeepSum())
print(len(variants))
