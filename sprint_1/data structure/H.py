class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
def solution(node):

    x = 0

    
    while x != None:
        x = node.next
        node.next = node.prev
        node.prev = x
        node = node.prev
        x = node.next

    node.next = node.prev
    node.prev = x

    head = node
    
    return head


