class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def solution(node, path = True):
    if node.left:
      if node.value > node.left.value:
        path = solution(node.left, path)
      else:
        return False
    if node.right:
      if node.value < node.right.value:
        path = solution(node.right, path)
      else:
        return False
    return path

