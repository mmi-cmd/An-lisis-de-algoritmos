def analizar_notas(estudiantes, notas, nota_aprobatoria, punto_extra, mostrar_detalle):
    """
    estudiantes: lista de nombres
    notas: lista de notas correspondientes
    nota_aprobatoria: nota mínima para aprobar
    punto_extra: puntos adicionales
    mostrar_detalle: booleano
    """

    # O(n) - calcular promedio
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)

    # O(n²) - contar aprobados comparando cada nota con todas
    aprobados = 0
    for i in range(len(notas)):
        for j in range(len(notas)):
            if i == j and notas[i] >= nota_aprobatoria:
                aprobados += 1

    # O(n²) - buscar notas repetidas
    repetidas = []
    for i in range(len(notas)):
        for j in range(i + 1, len(notas)):
            if notas[i] == notas[j]:
                repetidas.append(notas[i])

    # O(n log n) - ordenar notas
    notas_ordenadas = sorted(notas)

    # O(log n) - búsqueda binaria del promedio 
    inicio = 0
    fin = len(notas_ordenadas) - 1
    encontrada = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if notas_ordenadas[medio] == promedio:
            encontrada = True
            break
        elif notas_ordenadas[medio] < promedio:
            inicio = medio + 1
        else:
            fin = medio - 1

    # O(n³) - triple anidación 
    coincidencias = 0
    for nota in notas:
        for otra in notas:
            for tercera in notas:
                if nota == otra and otra == tercera:
                    coincidencias += 1

    # O(1)
    if mostrar_detalle:
        print("Promedio:", promedio)
        print("Aprobados:", aprobados)
        print("Notas repetidas:", repetidas)
        print("Coincidencias:", coincidencias)

    # O(n) - aplicar bonus
    total_ajustado = 0
    for nota in notas:
        total_ajustado += nota + punto_extra

    return total_ajustado, encontrada






def analizar_notas_optimizado(estudiantes, notas, nota_aprobatoria, punto_extra, mostrar_detalle):

    # O(n) - calcular suma y frecuencias al mismo tiempo
    suma = 0
    frecuencias = {}
    aprobados = 0

    for nota in notas:
        suma += nota
        frecuencias[nota] = frecuencias.get(nota, 0) + 1

        if nota >= nota_aprobatoria:
            aprobados += 1

    promedio = suma / len(notas)

    # O(1) promedio - verificar si el promedio existe
    encontrada = promedio in frecuencias

    # O(n) - detectar repetidas usando frecuencias
    repetidas = [nota for nota, freq in frecuencias.items() if freq > 1]    #Suma todas las cantidades de los elementos que aparecen más de una vez en la lista.

    # O(n log n) - ordenar una sola vez
    notas_ordenadas = sorted(notas)

    # Eliminamos el triple bucle innecesario 
    coincidencias = sum(freq for freq in frecuencias.values() if freq > 1)

    # O(1) - usar suma ya calculada
    total_ajustado = (suma + len(notas) * punto_extra)

    if mostrar_detalle:
        print(f"Promedio: {promedio}, Aprobados: {aprobados}")

    return total_ajustado, encontrada
