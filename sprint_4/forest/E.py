class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def solution(node1, node2, path=True):
    if not path:
        return False

    if node1.left and node2.left:
        path = solution(node1.left, node2.left, path)
    elif (node1.left and not node2.left) or (not node1.left and node2.left):
        return False

    if node1.right and node2.right:
        path = solution(node1.right, node2.right, path)
    elif (node1.right and not node2.right) or (not node1.right and node2.right):
        return False

    if node1.value != node2.value:
        return False

    return path

