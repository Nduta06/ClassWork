from collections import deque


class checkPalindrome:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

s = input()

obj = checkPalindrome()
for value in s:
    obj.push(value)
    obj.enqueue(value)

is_palindrome = True

for i in range(len(s) // 2):
    if obj.pop() != obj.dequeue():
        is_palindrome = False
        break

if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")