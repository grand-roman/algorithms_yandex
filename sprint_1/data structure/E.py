class Node:
    def __init__(self, value = None, next_item = None):
        self.value = value
        self.next_item = next_item
  
    def __str__(self):
        return self.value
    
def solution(node):
    while True:
        
        if node == None:
            break
        
        print(node.value)
        node = node.next_item

