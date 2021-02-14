# Iniciamos declarando las funciones
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

while True:
    try:
        op1=int(input("Introduce el primer número: "))
        op2=int(input("Introduce el segundo número: "))
        brak
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")

operacion=input("Que deseas hacer: \n1- Sumar \n2- Restar \n3- Multiplicar \n4- Dividir \n:")


