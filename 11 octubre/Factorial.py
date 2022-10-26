#Calcular el factorial
"""5! = 5*4*3*2*1"""
def factorial(num):
    if num == 1 & num ==0:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))
# Para mostrar las multiplicaciones que va haciendo
num = 5
while (num>0):
    print("El factorial de ",num, " es " ,factorial(num))
    num -= 1
