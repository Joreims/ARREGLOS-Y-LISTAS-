"""Buenas prácticas de programación"""
#Serie fibonacci
def serieFibo(num):
    if num > 1:
        return serieFibo(num -1)+ serieFibo(num-2)     
    return num
#Ciclos
for cont in range(6):
    print(serieFibo(cont), end=" - ")