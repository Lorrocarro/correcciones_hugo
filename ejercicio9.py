def calcular_factorial(n):
     factorial = 1
     for i in range(1, n+1):
         factorial *= i
     return factorial

print(calcular_factorial(5))
