#https://contest.yandex.ru/contest/18168/run-report/36950978/
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackQueue:
    def __init__(self):
        self.__in = Stack()
        self.__out = Stack()
        self.__size = 0

    def put(self, value):
        self.__size += 1
        self.__in.push(value)

    def get(self):
        if self.__size == 0:
            raise IndexError()
        elif not self.__out.is_empty():
            item = self.__out.pop()
        else:
            while not self.__in.is_empty():
                self.__out.push(self.__in.pop())

            item = self.__out.pop()

        self.__size -= 1
        return item

    def get_size(self):
        return self.__size


commands_n = int(input())

queue = StackQueue()

for _ in range(commands_n):
  command = input()

  if command.startswith("put"):
    n = int(command.split(" ")[1])
    queue.put(n)
  elif command == "get":
    if queue.get_size() == 0:
      print("error")
    else:
        print(str(queue.get()))
  elif command == "get_size":
    print(queue.get_size())
