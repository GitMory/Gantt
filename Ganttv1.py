class Proceso:
    def __init__(self, nombre, llegada, ejecucion):
        self.nombre = nombre
        self.llegada = llegada
        self.ejecucion = ejecucion
        self.inicio = 0
        self.finalizacion = 0
        self.retorno = 0
        self.espera = 0

def calcular_tiempos(procesos):
    tiempo_actual = 0
    for proceso in procesos:
        proceso.inicio = max(tiempo_actual, proceso.llegada)
        proceso.finalizacion = proceso.inicio + proceso.ejecucion
        proceso.retorno = proceso.finalizacion - proceso.llegada
        proceso.espera = proceso.inicio - proceso.llegada
        tiempo_actual = proceso.finalizacion

def mostrar_resultados(procesos):
    print("\nTabla de tiempos:")
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Proceso", "T. Llegada", "T. Ejecucion", "T. Retorno", "T. Espera"))
    for proceso in procesos:
        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(proceso.nombre, proceso.llegada, proceso.ejecucion, proceso.retorno, proceso.espera))

def mostrar_diagrama_gantt(procesos):
    print("\nDiagrama de Gantt:")
    gantt_chart = ""
    for proceso in procesos:
        gantt_chart += "-" * proceso.inicio + proceso.nombre + "-" * (proceso.finalizacion - proceso.inicio)
    print(gantt_chart)

def calcular_promedios(procesos):
    total_retorno = sum(proceso.retorno for proceso in procesos)
    total_espera = sum(proceso.espera for proceso in procesos)
    promedio_retorno = total_retorno / len(procesos)
    promedio_espera = total_espera / len(procesos)
    print("\nPromedio de Tiempo de Retorno:", promedio_retorno)
    print("Promedio de Tiempo de Espera:", promedio_espera)

def main():
    num_procesos = int(input("Ingrese el número de procesos: "))
    procesos = []
    
    for i in range(num_procesos):
        nombre = input(f"Ingrese el nombre del proceso {i + 1}: ")
        llegada = int(input(f"Ingrese el tiempo de llegada para el proceso {nombre}: "))
        ejecucion = int(input(f"Ingrese el tiempo de ejecucion para el proceso {nombre}: "))
        procesos.append(Proceso(nombre, llegada, ejecucion))

    procesos.sort(key=lambda x: x.llegada) 

    calcular_tiempos(procesos)
    mostrar_resultados(procesos)
    mostrar_diagrama_gantt(procesos)
    calcular_promedios(procesos)

if __name__ == "__main__":
    main()
