#Lectura de veinte valores enteros de un vetor denominado F.
valor = []
i = 1
while i<=20-1:
    val=int(input("Ingrese un valor del arreglo: "))
    valor.append(val)
    i= i+1
for val in valor:
    print(val)