class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value

class MyQueue:
    def __init__(self, maxs):
        self.head = Node()
        self.maxself = maxs

    def size(self):
        lenght = 0
        node = self.head
    
        if node.value == None:
            return lenght
    
        while node != None:
            lenght += 1
            node = node.next
        
        return lenght

    def push(self, value):
        node = self.head
        
        if self.size() >= self.maxself:
            print('error')
            return
        new_node = Node(value)
    
        if node.value == None:
            self.head = new_node
            return
        new_node.next = node
        self.head = new_node

    def pop(self):
        node = self.head
    
        if self.size() == 1:
            print(node)
            self.head =  Node()
            return
    
        if self.size() == 0:
            print('None')
            self.head =  Node()
            return
    
        while node.next != None:
            prev = node
            node = node.next
    
        prev.next = None
        print(node)

    def peek(self):
        node = self.head

        if self.size() == 0:
            return None
    
        while node.next != None:
            node = node.next
    
        return node


n = int(input())
m = int(input())
queue = MyQueue(m)

for i in range(n):
    command = input().split(' ')
    if command[0] == 'peek':
        print(queue.peek())

    if command[0] == 'pop':
        queue.pop()

    if command[0] == 'size':
        print(queue.size())

    if command[0] == 'push':
        queue.push(command[1])
