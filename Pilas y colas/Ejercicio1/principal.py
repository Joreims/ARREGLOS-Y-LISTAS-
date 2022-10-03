import Clases as ca
c = ca.ColadePaciente()
cod = 1

def menu():
    print("1. Agregar paciente.")
    print("2. Atender paciente.")
    print("3. Mostrar pacientes en espera.")
    print("4. Salir.")
    op = int(input("Escriba el # de la opcion: "))
    return op

def nuevoPaciente():
    global cod
    nom = input("Nombre del paciente: ")
    ape = input("Apellido del paciente: ")
    p = ca.Paciente(cod, nom, ape)
    cod +=1
    try:
        c.agregar(p)
    except Exception as ex:
        print(str(ex))
    
def atenderp():
    print("Paciente atendiendo:")
    print(c.quitar())

def listespera():
    for p in c.cola:
        print(p)

def main():
    op = 0
    while(op!=4):
        op = menu()
        if(op==1): nuevoPaciente()
        elif(op==2): atenderp()
        elif(op==3): listespera()
        elif(op==4): print("Adios...")
        else: print("Opcion invalida")
main()