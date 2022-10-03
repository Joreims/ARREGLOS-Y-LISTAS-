#Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
#estudiante de manera individual, escriba un código en Python que permita crear un correo
#electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
#“@est.uca.edu.ni”

nombre =input("Ingrese su primer nombre: ")
nombre2 =input("Ingrese su segundo nombre: ")
apellido =input("Ingrese su primer apellido: ")
apellido2 =input("Ingrese su segndo apellido: ")

print("Su correo institucional es: ", nombre+"."+apellido+"@est.uca.edu.ni")
