def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

notas = [85, 92, 78, 91, 88]
print("El promedio de las notas es:", calcular_promedio(notas))
