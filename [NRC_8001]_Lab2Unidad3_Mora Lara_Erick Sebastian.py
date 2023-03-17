
"""
    Descripción:
    Laboratorio: Algoritmo de Busqueda
    Autor:
    Erick Sebastian Mora 
"""

def costo(grafo, nodoInicio, nodoFin):
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

def todosCaminos(grafo, nodoInicio, nodoFin):
    caminos = []
    pila = [(nodoInicio, [nodoInicio])]
    while pila:
        nodoActual, camino = pila.pop()
        if nodoActual == nodoFin:
            caminos.append(camino)
        else:
            for nodo in grafo.get(nodoActual, []):
                if nodo not in camino:
                    pila.append((nodo, camino + [nodo]))
    return caminos

def imprimirRutas(inicio, fin, caminosPosible, costo):
    # Imprimir los costos
    print("Todos los caminos entre '{}' y '{}' son:".format(inicio, fin))
    for i, camino in enumerate(caminosPosible):
        print("Camino", i+1, ":", " -> ".join(camino))
        #print("Camino {}: {}".format(i+1, camino))

    print("El costo mínimo desde '{}' hasta '{}' es: {}".format(inicio, fin, costo))
# El grafo se representa como un diccionario de diccionarios

def generarGrafo():

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
    return grafo

if __name__ == '__main__':

    # Inicio y fin de las actividades
    inicio = 'Despertar'
    fin = 'Llegar a la Universidad'
    grafo = generarGrafo()
    caminosPosibles = todosCaminos(grafo, inicio, fin)
    costoMinimo = costo(grafo, inicio, fin)

    imprimirRutas(inicio, fin, caminosPosibles, costoMinimo)

