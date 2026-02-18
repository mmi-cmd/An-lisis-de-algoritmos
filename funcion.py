def analizar_ventas(ventas, costos, impuesto, descuento, meta, mostrar_detalle):
    """
    ventas: lista de ventas realizadas
    costos: lista de costos por producto
    impuesto: porcentaje de impuesto
    descuento: porcentaje de descuento
    meta: meta de ventas
    mostrar_detalle: booleano
    """

    # O(n) - calcular total de ventas
    total_ventas = 0
    for venta in ventas:
        total_ventas += venta

    # O(n²) - recalcular total innecesariamente varias veces
    suma_redundante = 0
    for i in range(len(ventas)):
        for j in range(len(ventas)):
            if i == j:
                suma_redundante += ventas[i]

    # O(n*m) - comparar cada venta con cada costo
    comparaciones = []
    for venta in ventas:
        for costo in costos:
            if venta > costo:
                comparaciones.append((venta, costo))

    # O(n*m*k) - triple anidación 
    coincidencias = 0
    for venta in ventas:
        for costo in costos:
            for otra_venta in ventas:
                if venta > costo and otra_venta == venta:
                    coincidencias += 1

    # O(n log n) - ordenar
    ventas_ordenadas = sorted(ventas)

    # O(log n) - búsqueda binaria
    inicio = 0
    fin = len(ventas_ordenadas) - 1
    encontrada = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if ventas_ordenadas[medio] == meta:
            encontrada = True
            break
        elif ventas_ordenadas[medio] < meta:
            inicio = medio + 1
        else:
            fin = medio - 1

    # O(n²) - buscar ventas repetidas
    repetidas = []
    for i in range(len(ventas)):
        for j in range(i + 1, len(ventas)):
            if ventas[i] == ventas[j]:
                repetidas.append(ventas[i])

    # O(1)
    if mostrar_detalle:
        print("Total ventas:", total_ventas)
        print("Comparaciones:", len(comparaciones))
        print("Coincidencias:", coincidencias)
        print("Ventas repetidas:", repetidas)

    # O(n) - aplicar impuesto elemento por elemento 
    total_con_impuesto = 0
    for venta in ventas:
        total_con_impuesto += venta * (1 + impuesto)

    total_final = total_con_impuesto - descuento

    return total_final, encontrada









def analizar_ventas_optimizado(ventas, costos, impuesto, descuento, meta, mostrar_detalle):
    # reducido en O(n)
    # Usar un diccionario de frecuencias para eliminar el bucle triple
    frecuencias = {}
    total_ventas = 0
    for v in ventas:
        total_ventas += v
        frecuencias[v] = frecuencias.get(v, 0) + 1
    

    # Búsqueda de meta reducido en O(1) promedio usando el set de frecuencias
    encontrada = meta in frecuencias 

    # Comparaciones O(n + m) 
    comparaciones_count = 0
    costos_ordenados = sorted(costos) # O(m log m)
    
    # Reduciendo O(n*m) a O(n log m)
    import bisect
    for venta in ventas:
        # Cuántos costos son menores que esta venta
        comparaciones_count += bisect.bisect_left(costos_ordenados, venta)    #biblioteca estándar utilizada para gestionar listas ordenadas de manera eficiente sin tener que reordenarlas constantemente tras cada inserción

    # 5. Coincidencias O(n * m) 
    coincidencias = 0
    for costo in costos:
        for v, freq in frecuencias.items():
            if v > costo:
                coincidencias += freq

    # 6. Cálculo final en O(1) usando el total_ventas ya calculado
    total_con_impuesto = total_ventas * (1 + impuesto)
    total_final = total_con_impuesto - descuento

    if mostrar_detalle:
        print(f"Total: {total_ventas}, Coincidencias: {coincidencias}")

    return total_final, encontrada