#Disminuir un numero hasta 0
"""def disminuir(num):
    if(num==0): print(0)
    else: 
        print(num)
        disminuir(num-1)

num = int(input("Dime un numero: "))
disminuir(num)"""

"""while num>= 0:
    print(num)
    num-=1"""
#Aumentar de un numero hasta 0

#def aumentar(n, num):
#    if(num==n): print(n)
#    else: 
#       print(num)
#        aumentar(num+1, n) 
#num = 0
#n= int(input("Dime un numero: "))
#aumentar(n, num)

#Imprimir los numeros de x hasta y

def imprimir(x,y):
    if (x==y):
        print(x,y)
    else:
        print(x,y)
        imprimir(x+1,y)
        
