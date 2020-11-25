class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def solution(node, path=float('-inf')):
    if node.left:
        path = solution(node.left, path)
    if node.right:
        path = solution(node.right, path)
    if path < node.value:
        path = node.value
    return path

