#Leer x cantidad de edades y mostrar el promedio de dichas edades.
nums = []
cant = int(input("Cuantas edades desea ingresar?: "))
i = 0
while i < cant:
    print("Edad: ",i+1)
    val = float(input())
    nums.append(val)
    i+=1
prom = sum(nums) / len(nums)
print("El promedio es: ",prom)
