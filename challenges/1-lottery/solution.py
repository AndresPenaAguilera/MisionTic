"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""


def solucion(b,n):

    cantidad_intentos = 0 

    while True:

        number_user = int(input("Ingrese un número:"))

        if n == number_user:
            cantidad_intentos += 1 
            print(f"¡LO LOGRASTE! Usaste {cantidad_intentos} intentos")
            break

        if( number_user < 0 or number_user > b):
            print("¡Te saliste del intervalo!"),
        else:
             if( number_user < n ):
                 cantidad_intentos += 1 
                 print("¡Ups! Estás por debajo")
             else:
                 cantidad_intentos += 1 
                 print("¡Ups! Te pasaste")

       
   
    

    

solucion(25,15)
    
"""
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN calcular_promedio_y_cuadro_honor(grupo) .
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA
"""