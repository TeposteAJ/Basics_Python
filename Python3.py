from ast import Pass
from urllib.parse import parse_qsl
import animales 

menu = {
    '1':' 1. Elefante',
    '2':' 2. Bisonte',
    '3':' 3. Tejon',
    '4':' 4. Cebra',
    '5':' 5. Panda',
    '0':' 0. Dejar de jugar'
}


class Animal:
    def __init__(self, type):
        self.type = type

    def mostrar_animal(self):
        animal_art = getattr(animales, self.type)
        return animal_art


if __name__ == '__main__':
    
    continuar = True
    print('SELECCIONA UN ANIMAL')
    print('')
    for elemento in menu:
        print(menu.get(elemento))        

    while continuar: 
        print('')
        opcion = input ('Ingresa tu opción:')
        if opcion == '0':
            continuar = False 
            print('')
            print('')
            print ('Gracias por jugar conmigo. Vuelve pronto')
            print(animales.dragon)

        elif opcion in menu: 
            menu_valor = menu.get(opcion)  # traigo la opcion escrita de animal seleccionado
            tipo_animal = menu_valor[4:]  #Le quito los primero 4 letras al menu, que es espacios y numeros

            #inicializando la classe
            animal = Animal(tipo_animal)

            #llamando al atributo
            imagen_animal = animal.mostrar_animal
            print(animal.mostrar_animal())
        else:
            print('')
            print ('Lo siento, la selección no fue válida.')
            print('Por favor prueba otra opción.')
            print('')
            
        
