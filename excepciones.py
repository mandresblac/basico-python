# Programa que realiza las 4 operaciones aritmeticas basicas con 2 números insertados por el usuario.

# Declaración de funciones
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación erronea"

# Inicio del programa
print()
print(" CALCULADORA BASICA CON DOS NÚMEROS ".center(136, "-"))

# Captura de datos
while True:
    try:
        op1=int(input("Introduce el primer número: "))
        op2=int(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")

print()
operacion=input("Que deseas hacer? \n1- Sumar \n2- Restar \n3- Multiplicar \n4- Dividir \n:")

# Estructura de control condicional
if operacion == "1":
    print(f"El resultado es: {suma(op1, op2)}")
elif operacion == "2":
    print(f"El resultado es: {resta(op1, op2)}")
elif operacion == "3":
    print(f"El resultado es: {multiplica(op1, op2)}")
elif operacion == "4":
    print(f"El resultado es: {divide(op1, op2)}")
else:
    print("Operación no contemplada")

# Salida del programa
print()
print("Programa terminado, ¡ADIOS!")
print("-" * 136)
