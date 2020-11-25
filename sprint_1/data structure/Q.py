class Dec:
    def __init__(self, maxs):
        self.items = [None for _ in range(maxs)]
        self.maxself = maxs
        self.tail = 0
        self.head = 0
        self.size = 0

    def size(self):
        return size

    def push_front(self, value):
        
        if self.size >= self.maxself:
            print('error')
            return
        
        self.size += 1
        self.head -= 1

        self.items[self.head % self.maxself] = value

    def push_back(self, value):
        
        if self.size >= self.maxself:
            print('error')
            return
        
        self.size += 1
        self.items[self.tail % self.maxself] = value
        self.tail += 1

    def pop_front(self):
        if self.size == 0:
            print('error')
            return

        item = self.items[self.head % self.maxself]

        self.head += 1
        self.size -= 1

        print(item)

    def pop_back(self):
        if self.size == 0:
            print('error')
            return

        self.tail -= 1
        self.size -= 1

        print(self.items[self.tail % self.maxself])


n = int(input())
m = int(input())
queue = Dec(m)

for i in range(n):
    command = input().split(' ')
    if command[0] == 'pop_back':
        queue.pop_back()

    if command[0] == 'pop_front':
        queue.pop_front()

    if command[0] == 'push_back':
        queue.push_back(command[1])
        
    if command[0] == 'push_front':
        queue.push_front(command[1])
