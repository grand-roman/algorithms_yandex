class Node:
    def __init__(self, value = None, next_item = None):
        self.value = value
        self.next_item = next_item
  
    def __str__(self):
        return self.value
    
def solution(node, index):

  if index == 0:
    return node.next_item

  head = node

  while index:
    if index == 1:
      pre_node = node

    node = node.next_item
    index -= 1

  pre_node.next_item = node.next_item

  return head

