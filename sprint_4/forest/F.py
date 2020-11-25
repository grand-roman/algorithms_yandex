from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def solution(node):
  results = []

  first_deque = deque()
  second_deque = deque()

  first_deque.append(node)

  while True:

    if first_deque:
      results.append(first_deque[0].value)

    while first_deque:
      current = first_deque.popleft()

      if current.left:
        second_deque.append(current.left)
      if current.right:
        second_deque.append(current.right)

    if second_deque:
      results.append(second_deque[0].value)

    while second_deque:
      current = second_deque.popleft()

      if current.left:
        first_deque.append(current.left)
      if current.right:
        first_deque.append(current.right)

    if not first_deque and not second_deque:
      break

  return results

