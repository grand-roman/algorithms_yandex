class Stack:
    def __init__(self):
        self.items = []
        self.count = 0
    
    def iterw(self):
        return self.items

    def push(self, item):
        self.items.append(item)
        self.count = self.count + 1
        
    def isEmpty(self):
         return self.items == []

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.count-1]
        
    def pop(self):
        if self.isEmpty():
            return None
            
        item = self.items.pop()
        self.count = self.count - 1
        if self.isEmpty():
            self.count = 0
        

string = input()

stack = Stack()

for bracket in string:
    if bracket == '{' or bracket == '(' or bracket == '[':
        stack.push(bracket)
        continue

    if bracket == '}':
        if stack.peek() == '{':
            stack.pop()
        else:
            stack.push(bracket)
            continue

    if bracket == ')':
        if stack.peek() == '(':
            stack.pop()
        else:
            stack.push(bracket)
            continue

    if bracket == ']':
        if stack.peek() == '[':
            stack.pop()
        else:
            stack.push(bracket)
            continue

if stack.isEmpty():
    print(True)
else:
    print(False)
