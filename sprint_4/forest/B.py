class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.left = left
    self.right = right


def solution(node, answer=True):
  if not answer:
    return answer

  mLright = 0
  mLleft = 0

  if node.right:
    mLright = newFindDepth(node.right) + 1
  if node.left:
    mLleft = newFindDepth(node.left) + 1

  if abs(mLright - mLleft) > 1:
    answer = False
  if node.left:
    answer = solution(node.left, answer)
  if node.right:
    answer = solution(node.right, answer)

  return answer

def newFindDepth(node, mLleft=0, mLright=0):
  if node.left and node.right:
    left = newFindDepth(node.left, mLleft + 1, mLright)
    right = newFindDepth(node.right, mLleft, mLright + 1)
    return left if left > right else right

  else:
    if node.left:
      return newFindDepth(node.left, mLleft + 1, mLright)
    
    if node.right:
      return newFindDepth(node.right, mLleft, mLright + 1)

  return mLleft + mLright

