class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value

class MyQueue:
    def __init__(self):
        self.head = Node()

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
            print('error')
            self.head =  Node()
            return
    
        while node.next != None:
            prev = node
            node = node.next
    
        prev.next = None
        print(node)


n = int(input())
queue = MyQueue()

for i in range(n):
    command = input().split(' ')

    if command[0] == 'get':
        queue.pop()

    if command[0] == 'size':
        print(queue.size())

    if command[0] == 'put':
        queue.push(command[1])
