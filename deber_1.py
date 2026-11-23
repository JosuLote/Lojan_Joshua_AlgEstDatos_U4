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


    return fusionar(izquierda, derecha)
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



def merge_sort(lista):
    #Merge Sort. Tiempo: O(n log n). Espacio adicional: O(n)
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return fusionar(izquierda, derecha) 

A = random.sample(range(1, 10**6), 1000)
#1
lista_copy = A.copy()
inicio = time.time()
insertion_sort(lista_copy)
fin = time.time()
print(f"Insertion sort tardó {fin - inicio:.6f} segundos")
#2
lista_copy = A.copy()
inicio = time.time()
merge_sort(lista_copy)
fin = time.time()
print(f"Merge sort tardó {fin - inicio:.6f} segundos")
