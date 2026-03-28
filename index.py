# --------- Task 1: Dynamic Array ---------
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [0] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [0] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print(self.arr[:self.size])


# --------- Node Class ---------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# --------- Task 2: Singly Linked List ---------
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, x):
        temp = self.head
        if temp and temp.data == x:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --------- Task 3: Stack ---------
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data if self.head else "Empty"


# --------- Task 3: Queue ---------
class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        return self.head.data if self.head else "Empty"


# --------- Task 4: Parentheses Checker ---------
def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            s.push(ch)
        elif ch in ")}]":
            if s.pop() != pairs[ch]:
                return False
    return s.head is None


# --------- MAIN TEST ---------
print("Dynamic Array:")
d = DynamicArray()
for i in range(10):
    d.append(i)
d.display()
print("Pop:", d.pop())
d.display()

print("\nLinked List:")
ll = SinglyLinkedList()
ll.insert_begin(10)
ll.insert_end(20)
ll.insert_end(30)
ll.display()
ll.delete(20)
ll.display()

print("\nStack:")
st = Stack()
st.push(1)
st.push(2)
print(st.pop())
print(st.peek())

print("\nQueue:")
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.front())

print("\nBalanced Parentheses:")
print(is_balanced("([])"))
print(is_balanced("([)]"))