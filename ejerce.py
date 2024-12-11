from datetime import datetime


#numeros = int(input("ingresar un numero"))

#if numeros % 2 == 0:
    #print("el numero es par")
#else:
    #print("el numero es impar")    




ano_nacimiento = int(input("coloca tu ano de nacimiento"))
 
ano_actual = datetime.now().year

edad = ano_actual - ano_nacimiento
print(f"tienes {edad} ano")



numero = int(input("escribe tu numero de tabla"))
print(f"tabla del {numero}:")
for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')


inicio = int(input("Tabla inicial: "))
fin = int(input("Tabla final: "))

for num in range(inicio, fin + 1):
    print(f"\nTabla del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
