class Node:
    def __init__(self, value = None, next_item = None):
        self.value = value
        self.next_item = next_item
  
    def __str__(self):
        return self.value
    
def solution(node, value):

  index = 0

  while node != None:

    if node.value == value:
      return index
    
    index += 1
    node = node.next_item
      

  return -1

