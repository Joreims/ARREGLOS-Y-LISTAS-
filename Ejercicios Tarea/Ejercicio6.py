#Leer 2 numeros y decir cual es mayor y cual es menor
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))


if num1 < num2:
    print("El numero mayor es: ",num2)
    print("El numero menor es: ",num1)
else:
    print("El numero mayor es: ",num1)
    print("El numero menor es: ",num2)