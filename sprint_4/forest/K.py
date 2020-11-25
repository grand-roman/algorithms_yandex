class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.left = left
    self.right = right


def solution(node, value='', result=0):
  if not node.left and not node.right:
    result += int(value + str(node.value))
    return result
  
  if node.left:
    result = solution(node.left, value + str(node.value), result)

  if node.right:
    result = solution(node.right, value + str(node.value), result)

  return result

