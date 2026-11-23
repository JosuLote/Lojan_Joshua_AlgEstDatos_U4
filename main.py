import random
import time
import statistics

from algoritmos import (
    insertion_sort,
    merge_sort,
    busqueda_lineal,
    busqueda_binaria,
)


# Mide un algoritmo de ordenamiento 3 veces y devuelve el promedio.
def medir(funcion, datos):
    tiempos = []

    for _ in range(3):
        copia = datos.copy()
        inicio = time.perf_counter()
        funcion(copia)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return statistics.mean(tiempos)


# Repite la busqueda para poder medir mejor su tiempo, que es muy pequeño.
def medir_busqueda(funcion, datos, objetivo):
    tiempos = []

    for _ in range(3):
        inicio = time.perf_counter()

        for _ in range(5000):
            funcion(datos, objetivo)

        fin = time.perf_counter()
        tiempos.append((fin - inicio) / 5000)

    return statistics.mean(tiempos)


# Muestra el tiempo y la razon respecto al tamaño anterior.
def mostrar_tabla(nombre, mediciones):
    print("\n" + nombre)
    print(f"{'n':>8} {'tiempo (s)':>15} {'razon':>10}")

    anterior = None
    for n, tiempo in mediciones:
        if anterior is None or anterior == 0:
            razon = "-"
        else:
            razon = f"{tiempo / anterior:.2f}"

        print(f"{n:>8} {tiempo:>15.8f} {razon:>10}")
        anterior = tiempo


def main():
    tamanos = [1000, 2000, 4000, 8000]

    tiempos_insercion = []
    tiempos_merge = []
    tiempos_lineal = []
    tiempos_binaria = []

    for n in tamanos:
        datos = random.sample(range(1, 10**6), n)

        # Medicion de los dos ordenamientos.
        tiempo = medir(insertion_sort, datos)
        tiempos_insercion.append((n, tiempo))

        tiempo = medir(merge_sort, datos)
        tiempos_merge.append((n, tiempo))

        # La busqueda binaria necesita una lista ordenada.
        lista_ordenada = merge_sort(datos)
        objetivo = lista_ordenada[-1]

        tiempo = medir_busqueda(busqueda_lineal, lista_ordenada, objetivo)
        tiempos_lineal.append((n, tiempo))

        tiempo = medir_busqueda(busqueda_binaria, lista_ordenada, objetivo)
        tiempos_binaria.append((n, tiempo))

    print("LABORATORIO DE EFICIENCIA DE ALGORITMOS")
    print("Los ordenamientos se miden 3 veces y se presenta el promedio.")
    print("Las busquedas se repiten 5000 veces por medicion y se presenta el promedio por busqueda.")

    mostrar_tabla("ORDENAMIENTO POR INSERCION - O(n^2)", tiempos_insercion)
    mostrar_tabla("MERGE SORT - O(n log n)", tiempos_merge)
    mostrar_tabla("BUSQUEDA LINEAL - O(n)", tiempos_lineal)
    mostrar_tabla("BUSQUEDA BINARIA - O(log n)", tiempos_binaria)


if __name__ == "__main__":
    main()
