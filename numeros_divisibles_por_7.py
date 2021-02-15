'''
Escriba un programa que encuentre todos los números divisibles por 7 pero no múltiplos de 5, entre 2000 y 3200 (ambos incluidos).
Los números obtenidos deben imprimirse en una secuencia separada por comas en una sola línea.

Sugerencias: considere usar el método range (#begin, #end)
'''
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(",".join(l))
