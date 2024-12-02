class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []
    
    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)
        else:
            print("Uno o ambos nodos no existen.")
    
    def mostrar_grafo(self):
        for nodo, conexiones in self.grafo.items():
            print(f"{nodo}: {', '.join(conexiones)}")


mi_grafo = Grafo()
ciudades = [
    "Manizales", "Pereira", "Armenia", "Chinchiná", "Villamaria", 
    "Palestina", "Neira", "La Virginia", "Dosquebradas", "Santa Rosa de Cabal",
    "Cartago", "Calarcá", "Ciscasia", "La Tebaida", "Montenegro"
]

for ciudad in ciudades:
    mi_grafo.agregar_nodo(ciudad)

mi_grafo.agregar_arista("Manizales", "Neira")
mi_grafo.agregar_arista("Manizales", "Palestina")
mi_grafo.agregar_arista("Manizales", "Villamaria")
mi_grafo.agregar_arista("Manizales", "Chinchiná")
mi_grafo.agregar_arista("Manizales", "Santa Rosa de Cabal")
mi_grafo.agregar_arista("Manizales", "Dosquebradas")
mi_grafo.agregar_arista("Manizales", "Pereira")
mi_grafo.agregar_arista("Manizales", "Cartago")
mi_grafo.agregar_arista("Manizales", "Armenia")
mi_grafo.agregar_arista("Santa Rosa de Cabal", "Pereira")
mi_grafo.agregar_arista("Santa Rosa de Cabal", "Armenia")
mi_grafo.agregar_arista("Dosquebradas", "Armenia")
mi_grafo.agregar_arista("Dosquebradas", "Pereira")
mi_grafo.agregar_arista("Dosquebradas", "Cartago")
mi_grafo.agregar_arista("La Virginia", "Pereira")
mi_grafo.agregar_arista("La Virginia", "Cartago")
mi_grafo.agregar_arista("Pereira", "Cartago")
mi_grafo.agregar_arista("Pereira", "Ciscasia")
mi_grafo.agregar_arista("Armenia", "Ciscasia")
mi_grafo.agregar_arista("Armenia", "Calarcá")
mi_grafo.agregar_arista("Armenia", "La Tebaida")
mi_grafo.agregar_arista("Armenia", "Montenegro")

mi_grafo.mostrar_grafo()