class Stack:
    def __init__(self):
        self.items = []
        self.setik = set()
        self.count = 0

    def push(self, item):
        if item not in self.setik:
            self.items.append(item)
            self.setik.add(item)
            self.count = self.count + 1
        
    def isEmpty(self):
         return self.items == []

    def peek(self):
        if self.isEmpty():
            print('error')
        else:
            print(self.items[self.count-1])
        
    def pop(self):
        if self.isEmpty():
            print('error')
            return None
            
        item = self.items.pop()
        self.setik.discard(item)
        self.count = self.count - 1
        if self.isEmpty():
            self.count = 0

    def size(self):
        return self.count
        

n = int(input())
stack = Stack()
for i in range(n):
    query = input().split(' ')
    if query[0] == 'peek':
        stack.peek()
    elif query[0] == 'push':
        stack.push(int(query[1]))
    elif query[0] == 'pop':
        stack.pop()
    elif query[0] == 'size':
        print(stack.size())
