#Calcular la media aritmetica, la moda y la media de x cantidad de edades
from statistics import mean, mode, median
import statistics
edades = [10, 20, 13, 15, 21, 23, 33, 12, 15]
suma = sum(edades)
mediana = statistics.median(edades)
media = statistics.mean(edades)
moda = statistics.mode(edades)
print("La moda es: ", moda)
print("La media es: ", media)
edadesOrdenadas = sorted(edades)
print(edades)
print("La mediana es: ", mediana)