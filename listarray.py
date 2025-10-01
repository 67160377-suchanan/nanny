class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ทดสอบการทำงาน
s = Stack()

print("Is empty?", s.is_empty())

# push ค่า 1-5
for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

# pop ค่าออกทั้งหมด
for i in range(5):
    print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())
