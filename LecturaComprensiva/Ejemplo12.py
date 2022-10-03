#Leer cien caracteres de un texto y contar el número de letras “b”.

import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

cadena = generate_random_string(100)

print(cadena)

print("Numero de letras b:", cadena.count("b") + cadena.count("B"))