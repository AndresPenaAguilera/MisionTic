#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la librería csv respectivamente
#from test import tester
import csv

"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""

def readerFile():
    csvfile = open('BTC-USD.csv','r', newline='', encoding='utf-8')
    data = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    return data

def getDataNewFile(data):

    results = []
    Indice = 0
    fecha_menor_precio = ''
    menor_precio = -1
    fecha_mayor_precio = ''
    mayor_precio = -1
    menor_precio_ant =0
    Variacion_diaria = 0
    sum_Variacion_diaria=0

    results.append(['Indice', 'Fecha', 'Open', 'Close', 'Variacion_diaria', 'Descripcion'])
    
    for row in data:
       
        if row[0] != 'Date':

            
            fecha = row[0]
            Variacion_diaria =  float(row[4]) - float(row[1])
            sum_Variacion_diaria = sum_Variacion_diaria + Variacion_diaria
            
            

            if Variacion_diaria>0:
                descripcion = 'Sube'
            
            if Variacion_diaria==0:
                descripcion = 'Estable'
            
            if Variacion_diaria<0:
                descripcion = 'Baja'

            results.append( [ Indice, fecha, row[1], row[4], Variacion_diaria, descripcion ] )

            if menor_precio == -1:
                menor_precio = row[3]
                fecha_menor_precio = fecha
                menor_precio_ant = row[3]
            else:
                if menor_precio_ant > row[3]:
                    menor_precio = row[3]
                    fecha_menor_precio = fecha
                    menor_precio_ant = row[3]

            if mayor_precio == -1:
                mayor_precio = row[2]
                fecha_mayor_precio = fecha
                mayor_precio_ant = row[2]
            else:
                if mayor_precio_ant < row[2]:
                    mayor_precio = row[2]
                    fecha_mayor_precio = fecha
                    mayor_precio_ant = row[2]

            Indice = Indice + 1
       
      
    variacion_diaria_media = ( sum_Variacion_diaria / (Indice + 1) )
           
    return (results, str(fecha_menor_precio), float(menor_precio), str(fecha_mayor_precio), float(mayor_precio), float(variacion_diaria_media))




def createNewFile(newData):

    with open('analisis_bitcoin.csv','w',newline="") as csvNewFile:
        writer = csv.writer(csvNewFile, delimiter=';', skipinitialspace=True)

        for val in newData:
            writer.writerow(val)
            
        csvNewFile.close()


"""Fin espacio para programar funciones propias"""

def solucion():

    data = readerFile()
    NewData = getDataNewFile(data)
    createNewFile(NewData[0])
    

    return NewData[1], NewData[2], NewData[3], NewData[4], NewData[5]

print(solucion())
"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED DESARROLLE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#tester(solucion)