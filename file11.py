
'''
11. Write a python program that generates the first n numbers in the
Fibonacci sequence.
'''

def fibonacci(n):
    fib_seq = []
    p, q = 0, 1
    for _ in range(n):
        fib_seq.append(q)
        p, q = q, p + q
    return fib_seq
n = int(input("Enter  Fibonacci numbers to generate: "))

fib_num = fibonacci(n)
print("The first", n, "Fibonacci numbers are:", fib_num)
