class AFD:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales

    def evaluar(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False
            estado_actual = self.transiciones.get((estado_actual, simbolo))
            if estado_actual is None:
                return False
        return estado_actual in self.estados_finales

    @classmethod
    def cargar_automata(cls, nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            lineas = [line.strip() for line in archivo.readlines() if line.strip()]
        
        alfabeto = lineas[0].split()
        num_estados = int(lineas[1])
        estados = lineas[2].split()
        estado_inicial = lineas[3]
        num_estados_finales = int(lineas[4])
        estados_finales = lineas[5:num_estados_finales+5]

        transiciones = {}
        for linea in lineas[num_estados_finales+5:]:
            partes = linea.split()
            if len(partes) == 3:
                estado_origen, simbolo, estado_destino = partes
                transiciones[(estado_origen, simbolo)] = estado_destino

        return cls(estados, alfabeto, transiciones, estado_inicial, estados_finales)

def main():
    nombre_archivo = input("Ingrese el nombre del archivo del autÃ³mata: ")
    automata = AFD.cargar_automata(nombre_archivo)

    while True:
        cadena = input("Ingrese una cadena para evaluar: ")
        if cadena.lower() == "salir":
            break
        if automata.evaluar(cadena):
            print(f"La cadena '{cadena}' es RECONOCIDA")
        else:
            print(f"La cadena '{cadena}' NO es reconocida")

if __name__ == "__main__":
    main()