import time
import random

def insertion_sort(lista):
    #Ordenamiento por inserción. Tiempo promedio y peor: O(n^2). Espacio: O(1)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = actual

    return lista


def merge_sort(lista):
    #Merge Sort. Tiempo: O(n log n). Espacio adicional: O(n)
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return fusionar(izquierda, derecha)

#f apoyo unir unitarios
def fusionar(a, b):
    resultado = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    return resultado + a[i:] + b[j:]


def busqueda_lineal(lista, objetivo):
    """Busqueda lineal. Tiempo: O(n). Espacio adicional: O(1)."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    """Busqueda binaria (lista ordenada). Tiempo: O(log n). Espacio: O(1)."""
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


for nombre, n in [("Pequeña", 20), ("Grande", 1_000_000)]:
    lista = list(range(n))
    objetivo = -1  # peor caso

    t0 = time.perf_counter()
    busqueda_lineal(lista, objetivo)
    t_lin = time.perf_counter() - t0

    t0 = time.perf_counter()
    busqueda_binaria(lista, objetivo)
    t_bin = time.perf_counter() - t0

    print(f"{nombre} ({n}): lineal={t_lin:.8f}s | binaria={t_bin:.8f}s")
    