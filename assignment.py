# -------------------- Stack ADT --------------------
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -------------------- Factorial --------------------
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)


# -------------------- Fibonacci --------------------
# Naive Fibonacci
fib_calls_naive = 0
def fib_naive(n):
    global fib_calls_naive
    fib_calls_naive += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# Memoized Fibonacci
fib_calls_memo = 0
memo = {}

def fib_memo(n):
    global fib_calls_memo
    fib_calls_memo += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


# -------------------- Tower of Hanoi --------------------
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)


# -------------------- Binary Search --------------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)


# -------------------- MAIN --------------------
if __name__ == "__main__":
    
    print("----- Stack ADT -----")
    s = StackADT()
    s.push(10)
    s.push(20)
    print("Top:", s.peek())
    print("Pop:", s.pop())
    print("Size:", s.size())

    print("\n----- Factorial -----")
    print("5! =", factorial(5))
    print("10! =", factorial(10))

    print("\n----- Fibonacci -----")
    n = 10
    fib_calls_naive = 0
    print("Naive:", fib_naive(n), "Calls:", fib_calls_naive)

    fib_calls_memo = 0
    memo = {}
    print("Memo:", fib_memo(n), "Calls:", fib_calls_memo)

    print("\n----- Tower of Hanoi (N=3) -----")
    hanoi(3, 'A', 'B', 'C')

    print("\n----- Binary Search -----")
    arr = [1,3,5,7,9,11,13]
    print("Search 7:", binary_search(arr, 7, 0, len(arr)-1))
    print("Search 2:", binary_search(arr, 2, 0, len(arr)-1))
    