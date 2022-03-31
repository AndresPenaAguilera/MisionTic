#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, 
#y el funcionamiento de la librería csv respectivamente
#from test import tester
import csv
"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""



"""Inicio espacio para programar funciones propias"""

def readerFile():
    csvfile = open('COVCOL.csv','r', newline='', encoding='utf-8')
    data = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    return data

def getDataNewFile(data):
    results = []
    age_youngest = -1
    age_ant = 0
    unit_youngest = -1
    counter = 0
    sumEdad = 0
    results.append(['Sexo', 'Edad en agnos','Concepto'])
    
    for row in data:

        if row[7] != 'Sexo':

            age = int(row[5])
            originalAge = int(row[5])
            UnitMeasureAge = int(row[6])
            sexo = row[7].strip()

            if age<0:
                age =0
                
            if UnitMeasureAge==2 and age>0:
                 age = int(age/12)
            
            if UnitMeasureAge==3 and age>0:
                 age = int(age/360)

            if age_youngest == -1:
                age_youngest = originalAge
                unit_youngest = UnitMeasureAge
                age_ant = age
            else:
                if age_ant > age:
                    age_youngest = originalAge
                    unit_youngest = UnitMeasureAge
                    age_ant = age

        
            if UnitMeasureAge==1 and age>18 and row[8]!='Fallecido':
                counter = counter + 1
                sumEdad = sumEdad + age
            
            concept = getConcept( age, UnitMeasureAge )
            results.append( [sexo, age, concept.strip()] )
            
        
    
    mean_alive_g = float(sumEdad/counter)

    return (results, int(age_youngest), float(unit_youngest), mean_alive_g)

def getConcept(edad, unidadMedidaEdad):

    if unidadMedidaEdad != 1:
        return 'Primera infancia'
    
    if edad<=5:
        return 'Primera infancia'

    if edad>=6 and edad<=11:
        return 'Infante'
    
    if edad>=12 and edad<=17:
        return 'Adolescente'
    
    if edad>=18 and edad<=59:
        return 'Adulto'
    
    return 'Persona mayor'


def createNewFile(newData):

    with open('analisis_covcol.csv','w',newline="") as csvNewFile:
        writer = csv.writer(csvNewFile, delimiter=';', skipinitialspace=True)

        for val in newData:
            writer.writerow(val)
            
        csvNewFile.close()


"""Fin espacio para programar funciones propias"""

def solucion():
    data = readerFile()
    tuplaNewData = getDataNewFile(data)
    createNewFile(tuplaNewData[0])

    
    age_youngest  = tuplaNewData[1]
    unit_youngest = tuplaNewData[2]
    mean_alive_g  = tuplaNewData[3]
    
    return age_youngest, unit_youngest, mean_alive_g


print(solucion())
"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED DESARROLLE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#tester(solucion)