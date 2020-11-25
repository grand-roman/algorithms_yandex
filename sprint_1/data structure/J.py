class N:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    

class Node:
    def __init__(self):
        self.tail = N()
        self.head = self.tail
    
    def is_empty(self):
        return self.head == self.tail
        
    def first(self):
        return self.head
        
    def __str__(self):
        return self.value

    def insert(self, value, before=0):
        node = N(value)

        if before <= 0 or self.is_empty():
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            before_node = self.__find_by_index(before)

            before_node.prev.next = node
            node.prev = before_node.prev

            before_node.prev = node
            node.next = before_node
        
    def pop(self, index=0):
        if index == 0:
            first = self.head
            self.head = first.next

            return first.value
        else:
            pop_node = self.__find_by_index(index)

            pop_node.prev.next = pop_node.next
            pop_node.next.prev = pop_node.prev

            return pop_node.value


class Stack:
    def __init__(self):
        self.items = []
        self.tracking_max = Node()

    def push(self, item):
        if self.tracking_max.is_empty() or item >= self.get_max():
            self.tracking_max.insert(item)
        self.items.append(item)
        
    def isEmpty(self):
         return self.items == []

    def pop(self):
        if self.isEmpty():
            print('error')
            return None
            
        item = self.items.pop()
        
        if item == self.get_max():
            self.tracking_max.pop()
        
    def get_max(self):
        return self.tracking_max.first().value

n = int(input())
stack = Stack()
for i in range(n):
    query = input().split(' ')
    if query[0] == 'get_max':
        print(stack.get_max())
    elif query[0] == 'push':
        stack.push(int(query[1]))
    elif query[0] == 'pop':
        stack.pop()
