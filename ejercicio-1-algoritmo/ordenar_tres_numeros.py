```python
# Ejercicio 1: Ordenar tres números de menor a mayor
# IA | Semana 1


def ordenar_tres_numeros(a, b, c):
    # 1 con 2
    if a > b:
        a, b = b, a

    # 2 con el 3
    if b > c:
        b, c = c, b

    # 1 con 2 otra vez
    if a > b:
        a, b = b, a

    return a, b, c


def mostrar_proceso(a, b, c):
    print("\nEntrada:", a, b, c)
    print("numeros iniciales:", a, b, c)

    # 1
    print("\npaso 1: Comparar", a, "y", b)
    if a > b:
        a, b = b, a
        print("Se intercambian:", a, b, c)
    else:
        print("No es necesario intercambiar:", a, b, c)

    # 2
    print("\nPaso 2: Comparar", b, "y", c)
    if b > c:
        b, c = c, b
        print("Se intercambian:", a, b, c)
    else:
        print("No es necesario intercambiar:", a, b, c)

    # Tercer paso
    print("\nPaso 3: Comparar", a, "y", b)
    if a > b:
        a, b = b, a
        print("se intercambian:", a, b, c)
    else:
        print("no es necesario intercambiar:", a, b, c)

    print("\nresultado final:", a, b, c)

    return a, b, c


if __name__ == "__main__":

    print("EJERCICIO 1: ORDENAR TRES NUMEROS")

    # Pruebas del ejercicio
    mostrar_proceso(7, 2, 5)
    mostrar_proceso(2, 2, 9)
    mostrar_proceso(9, 5, 1)

    # Otros casos para comprobar que funciona
    mostrar_proceso(3, 3, 3)
    mostrar_proceso(1, 2, 3)

    # Comprobar varios resultados
    print("\nVERIFICACION DE RESULTADOS")

    casos = [
        (7, 2, 5),
        (2, 2, 9),
        (9, 5, 1),
        (3, 3, 3),
        (1, 2, 3),
        (5, 1, 5),
        (10, 0, -3)
    ]

    todos_ok = True

    for a, b, c in casos:
        resultado = ordenar_tres_numeros(a, b, c)
        esperado = tuple(sorted([a, b, c]))

        if resultado == esperado:
            print("Correcto:", (a, b, c), "->", resultado)
        else:
            print("Error:", (a, b, c), "->", resultado)
            todos_ok = False

    if todos_ok:
        print("\ntodas las pruebas salieron bien.")
    else:
        print("\nalgunas pruebas tuvieron errores.")
```