from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.right = right
    self.left = left

def solution(node):
  q_right = deque()
  q_left = deque()

  left = node.left
  right = node.right

  if left is None and right is None:
    return True
  
  if (left is None and right is not None) or (right is None and left is not None):
    return False

  q_right.append(right)
  q_left.append(left)

  while q_right and q_left:
    current_right = q_right.popleft()
    current_left = q_left.popleft()

    if current_right.value != current_left.value:
      return False

    if current_right.left and current_left.right:
      q_right.append(current_right.left)
      q_left.append(current_left.right)
    elif (current_left.right is None and current_right.left is not None) or (current_right.left is None and current_left.right is not None):
      return False

    if current_right.right and current_left.left:
      q_right.append(current_right.right)
      q_left.append(current_left.left)
    elif (current_left.left is None and current_right.right is not None) or (current_right.right is None and current_left.left is not None):
      return False

  return True

