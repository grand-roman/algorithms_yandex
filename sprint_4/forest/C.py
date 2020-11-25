from collections import deque

class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.left = left
    self.right = right

def solution(node):
  result = []

  first_q = deque()
  second_q = deque()

  first_q.append(node)

  while True:
    intermediate = []

    while first_q:
      current = first_q.popleft()
      intermediate.append(current.value)

      if current.left:
        second_q.append(current.left)
      if current.right:
        second_q.append(current.right)

    result.append(intermediate)

    intermediate = []
    first_q.clear()

    while second_q:
      current = second_q.popleft()
      intermediate.append(current.value)

      if current.left:
        first_q.append(current.left)
      if current.right:
        first_q.append(current.right)

    result.append(intermediate)

    second_q.clear()

    if not first_q and not second_q:
      break

  return result

