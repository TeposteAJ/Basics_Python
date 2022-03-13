#Función que suma un arreglo menor de 1000 elementos. 
import random

lista =[]
#Creando un arreglo de numeros a# entre los valores de 3 a 93, con saltos de 1leatorios de 683 elementos
for i in range(123):
    lista.append(random.randint(1, 239))


#Definiendo la función 
def SumArr(arreglo):
    suma=0
    for element in arreglo: 
        suma += element
    return suma


#llamando la función para sumar el arreglo e imprimiendo la respuesta
print("La suma de los componentes del arreglo es" , SumArr(lista))
print("Valor correcto:", sum(lista)) #Valor para comprobar, con funcion predefinida
