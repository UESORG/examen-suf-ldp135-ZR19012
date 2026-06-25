import json

def importar_y_validar_orden(json_orden):
    try:
        orden = json.loads(json_orden)
        if "items" not in orden or "total" not in orden:
            raise KeyError("Faltan llaves requeridas: 'items' o 'total'")
        if orden["total"] <= 0:
            raise ValueError("El campo 'total' debe ser mayor a 0")
        return orden
    except (KeyError, ValueError):
        return None
    except Exception:
        return None

def gestionar_historial_carrito(historial_pila, accion, item=None):
    if accion == "AGREGAR":
        historial_pila.append(item)
    elif accion == "DESHACER":
        if len(historial_pila) == 0:
            return None
        return historial_pila.pop()

def escanear_estanteria_bodega(matriz_bodega, fila_centro, col_centro):
    contador = 0
    for i in range(fila_centro - 1, fila_centro + 2):
        for j in range(col_centro - 1, col_centro + 2):
            if i >= 0 and i < len(matriz_bodega):
                if j >= 0 and j < len(matriz_bodega[i]):
                    if matriz_bodega[i][j] == 1:
                        contador += 1
    return contador

def calcular_descuento_cascada(nodo_descuento):
    if "porcentaje_final" in nodo_descuento:
        return nodo_descuento["porcentaje_final"]
    if nodo_descuento["cliente_frecuente"] == True:
        return calcular_descuento_cascada(nodo_descuento["derecha"])
    else:
        return calcular_descuento_cascada(nodo_descuento["izquierda"])

def ordenar_productos_quicksort(lista_items):
    if len(lista_items) <= 1:
        return lista_items
    pivote = lista_items[len(lista_items) // 2]
    menores = [item for item in lista_items if item["precio"] < pivote["precio"]]
    iguales = [item for item in lista_items if item["precio"] == pivote["precio"]]
    mayores = [item for item in lista_items if item["precio"] > pivote["precio"]]
    return ordenar_productos_quicksort(menores) + iguales + ordenar_productos_quicksort(mayores)

def buscar_precio_binario(lista_ordenada, precio_buscado):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio]["precio"] == precio_buscado:
            return medio
        elif lista_ordenada[medio]["precio"] < precio_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
