def fibonacci(n):
    if n <= 0:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print([fibonacci(i) for i in range(10)])
