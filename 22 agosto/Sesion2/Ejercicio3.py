#Leer un numero del 1 al 7 e imprimir el dia
#correspondiente a la semana

num = int(input("Dime un # del 1 al 7"))
if num>= 1 and num<=7:
    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Lunes")
    elif num == 3:
        print("Martes")
    elif num == 4:
        print("Miercoles")
    elif num == 5:
        print("Jueves")
    elif num == 6:
        print("Viernes")
    elif num== 7:
        print("Sabado")
else:
    print("El numero debe estar entre 1 y 7")

