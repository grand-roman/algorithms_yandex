class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def solution(node, mLleft = 0, mLright = 0):
    if node.left and node.right:
      left = solution(node.left, mLleft + 1, mLright)
      right = solution(node.right, mLleft, mLright + 1)
      return left if left > right else right

    if node.left:
      return solution(node.left, mLleft + 1, mLright)

    if node.right:
      return solution(node.right, mLleft, mLright + 1)

    return mLleft + mLright + 1

