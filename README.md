[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/66UDLJ0P)
# ZR19012 - Josué Emanuel Zúniga Ramírez - GT01

## E-Commerce Pro - Backend Transaccional

Examen Complementario de Lógica de Programación

---

## Descripción

Este proyecto implementa el backend transaccional de la plataforma **E-Comerce Pro**, aplicando algoritmos de búsqueda, ordenamiento, recursividad y estructuras de datos para gestionar carritos de compra, historiales y ubicaciones de inventario.

---

## Archivos

| Archivo | Descripción |
|---|---|
| `carrito_pro.py` | Módulo principal con las 6 funciones del backend |
| `test_carrito_pro.py` | Suite de pruebas unitarias con pytest |

---

## carrito_pro.py

Contiene exactamente 6 funciones:

### 1. `importar_y_validar_orden(json_orden)`
Decodifica un string JSON y valida que contenga las llaves `"items"` y `"total"`, y que `"total"` sea mayor a 0. Utiliza bloques `try/except` para capturar errores de formato (`KeyError`, `ValueError`) y retorna el diccionario si es válido, o `None` en caso de fallo.

### 2. `gestionar_historial_carrito(historial_pila, accion, item=None)`
Maneja una lista como una **Pila LIFO**. Si la acción es `"AGREGAR"` inserta el ítem al final con `append`. Si es `"DESHACER"` extrae y retorna el último ítem con `pop`, o retorna `None` si la pila está vacía. La lista se muta por referencia.
 
### 3. `escanear_estanteria_bodega(matriz_bodega, fila_centro, col_centro)`
Recorre la **vecindad 3×3** alrededor de una coordenada dada en una matriz bidimensional. Usa ciclos `for` anidados y valida los límites de la matriz para evitar desbordamientos, retornando la cantidad de celdas con valor `1` encontradas en esa área.
 
### 4. `calcular_descuento_cascada(nodo_descuento)`
Recorre un **árbol binario** representado como diccionarios anidados. Si el nodo contiene la llave `"porcentaje_final"` lo retorna directamente (caso base). Si `"cliente_frecuente"` es `True` desciende por `"derecha"`, de lo contrario por `"izquierda"`, usando recursividad.
 
### 5. `ordenar_productos_quicksort(lista_items)`
Ordena una lista de diccionarios por la llave `"precio"` de menor a mayor usando el algoritmo **QuickSort**. Selecciona un pivote central y divide la lista en sublistas mediante listas por comprensión, combinándolas recursivamente.
 
### 6. `buscar_precio_binario(lista_ordenada, precio_buscado)`
Realiza una **búsqueda binaria** sobre una lista de diccionarios ya ordenada por precio. Usa un ciclo `while` con punteros `izquierda`, `derecha` y `medio` para localizar el precio en tiempo logarítmico. Retorna el índice encontrado, o `-1` si no existe.
 
---

## test_carrito_pro.py

He creado **30 pruebas unitarias** escritas con `pytest`, organizadas por función y cubriendo los siguientes escenarios:

| Función probada | Casos cubiertos |
|---|---|
| `importar_y_validar_orden` | JSON válido, sin llave `items`, sin llave `total`, total cero, total negativo, JSON corrupto |
| `gestionar_historial_carrito` | Agregar un ítem, agregar múltiples, deshacer retorna último, deshacer pila vacía, mutación por referencia |
| `escanear_estanteria_bodega` | Centro de matriz, esquina superior izquierda, esquina inferior derecha, sin unos, borde derecho |
| `calcular_descuento_cascada` | Caso base directo, cliente frecuente (derecha), no frecuente (izquierda), recursión multinivel |
| `ordenar_productos_quicksort` | Lista desordenada, lista vacía, un elemento, precios iguales, ya ordenada |
| `buscar_precio_binario` | Precio existente, precio inexistente, primer elemento, último elemento, lista vacía |

---

## Ejecución local

```bash
# Instalar dependencias
pip install pytest
 
# Correr las pruebas
pytest test_carrito_pro.py -v
```
 
---
 
## Tecnologías
 
- Python 3
- pytest
- Módulo `json` (stdlib)


