# https://contest.yandex.ru/contest/18168/run-report/36868378/

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item == '-' or item == '+' or item == '*' or item == '/':
            self.operation(item)
        else:
            self.items.append(item)

    def operation(self, oper):
        first = int(self.items.pop())
        second = int(self.items.pop())
    
        if oper == '-':
            result = second - first
        if oper == '+':
            result = second + first
        if oper == '*':
            result = second * first
        if oper == '/':
            result = int(round(second // first))
    
        self.push(result)

    def peek(self):
        return self.items[len(self.items) - 1]
        
stack = Stack()
put = input().split(' ')
for item in put:
    stack.push(item)
print(stack.peek())
