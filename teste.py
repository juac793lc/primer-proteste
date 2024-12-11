# Pedir tres números al usuario
num1 = int(input("Escribe un número 1: "))
num2 = int(input("Escribe un número 2: "))
num3 = int(input("Escribe un número 3: "))

# Comparar los números para encontrar el mayor
if num1 == num2 == num3:
    print("Todos los números son iguales.")
else:
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
    else:
        mayor = num3
    print(f"El número mayor es: {mayor}")
