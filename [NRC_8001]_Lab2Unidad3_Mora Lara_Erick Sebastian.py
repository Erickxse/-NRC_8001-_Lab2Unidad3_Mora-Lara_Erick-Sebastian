
"""
    Descripción:
    Laboratorio: Algoritmo de Busqueda
    Autor:
    Erick Sebastian Mora 
"""

def busqueda(grafo, nodoInicio, nodoFin):
    #Funcion de busqueda para encontrar el camino mas rapido
    costos = {}
    #Se crea un diccionario vacio para almacenar los costos de cada nodo
    for nodo in grafo:
        costos[nodo] = float('inf')
        #Se inicializa el diccionario 'costos' con el valor infinito
        #Se inicializa con el valor mas alto posible con el objetivo de encontrar el costo minimo mas tarde
    costos[nodoInicio] = 0 #El nodo inicial no tiene costo 
    cola = [nodoInicio]
    #Se inicia una cola, con el primer nodo 
    while cola:
        nodoActual = cola.pop(0)
        if nodoActual == nodoFin:
            return costos[nodoFin]
        for nodoAsociado, costoCambio in grafo[nodoActual].items():
            nuevoCosto = costos[nodoActual] + costoCambio
            if nuevoCosto < costos[nodoAsociado]:
                costos[nodoAsociado] = nuevoCosto
                cola.append(nodoAsociado)


# El grafo se representa como un diccionario de diccionarios

if __name__ == '__main__':

    grafo ={
        'Despertar' : {'Levantarse': 1},
        'Levantarse' : {'Ducharse': 1 , 'Vestirse': 1},
        'Ducharse' : {'Vestirse' : 1},
        'Vestirse' : {'Desayunar': 1},
        'Desayunar' : {'Salir de Casa': 1},
        'Salir de Casa' : {'Tomar Taxi' : 1, 'Tomar Bus' : 1, 'Auto Propio' : 1},
        'Tomar Taxi' : {'Llegar a la Universidad' : 1},
        'Tomar Bus' : {'Transbordar' : 1},
        'Auto Propio' : {'Estacionar' : 1},
        'Transbordar' : {'Llegar a la Universidad' : 1},
        'Estacionar' : {'Llegar a la Universidad' : 1},
        'Llegar a la Universidad' : {'Asistir a Estadistica' : 1 , 'Asistir a Modelos' : 1},
        'Asistir a Estadistica' : {'Asistir a Modelos' : 1},
        'Asistir a Modelos' : {},

    }

    # Inicio y fin de las actividades
    inicio = 'Despertar'
    fin = 'Asistir a Modelos'

# Ejecutar el algoritmo y almacenar el costo mínimo
costoMinimo = busqueda(grafo, inicio, fin)

# Imprimir los costos
print("El costo mínimo desde '{}' hasta '{}' es: {}".format(inicio, fin, costoMinimo))