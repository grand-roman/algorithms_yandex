class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        
    def isEmpty(self):
         return self.items == []

    def pop(self):
        if self.isEmpty():
            print('error')
        else:
            return self.items.pop()
        
    def get_max(self):
        if self.isEmpty():
            return None
        return max(self.items)

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
