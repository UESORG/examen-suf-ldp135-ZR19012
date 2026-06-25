import pytest

from carrito_pro import (
    importar_y_validar_orden,
    gestionar_historial_carrito,
    escanear_estanteria_bodega,
    calcular_descuento_cascada,
    ordenar_productos_quicksort,
    buscar_precio_binario,
)


#Tests: importar_y_validar_orden

def test_orden_valida():
    json_valido = '{"items": ["laptop", "mouse"], "total": 150.0}'
    resultado = importar_y_validar_orden(json_valido)
    assert resultado is not None
    assert resultado["total"] == 150.0


def test_orden_sin_llave_items():
    json_sin_items = '{"total": 100}'
    resultado = importar_y_validar_orden(json_sin_items)
    assert resultado is None


def test_orden_sin_llave_total():
    json_sin_total = '{"items": ["teclado"]}'
    resultado = importar_y_validar_orden(json_sin_total)
    assert resultado is None


def test_orden_total_cero():
    json_total_cero = '{"items": ["monitor"], "total": 0}'
    resultado = importar_y_validar_orden(json_total_cero)
    assert resultado is None


def test_orden_total_negativo():
    json_total_negativo = '{"items": ["silla"], "total": -50}'
    resultado = importar_y_validar_orden(json_total_negativo)
    assert resultado is None


def test_json_corrupto():
    json_corrupto = '{"items": ["silla", "total": 100}'
    resultado = importar_y_validar_orden(json_corrupto)
    assert resultado is None


#Tests: gestionar_historial_carrito

def test_agregar_item_a_pila():
    pila = []
    gestionar_historial_carrito(pila, "AGREGAR", "camisa")
    assert pila == ["camisa"]


def test_agregar_multiples_items():
    pila = []
    gestionar_historial_carrito(pila, "AGREGAR", "camisa")
    gestionar_historial_carrito(pila, "AGREGAR", "pantalon")
    assert pila == ["camisa", "pantalon"]


def test_deshacer_retorna_ultimo():
    pila = ["camisa", "pantalon"]
    resultado = gestionar_historial_carrito(pila, "DESHACER")
    assert resultado == "pantalon"
    assert pila == ["camisa"]


def test_deshacer_pila_vacia():
    pila = []
    resultado = gestionar_historial_carrito(pila, "DESHACER")
    assert resultado is None


def test_mutacion_pila_por_referencia():
    pila = []
    gestionar_historial_carrito(pila, "AGREGAR", "zapatos")
    assert len(pila) == 1


#Tests: escanear_estanteria_bodega

def test_contar_unos_centro():
    matriz = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    resultado = escanear_estanteria_bodega(matriz, 1, 1)
    assert resultado == 5


def test_contar_esquina_superior_izquierda():
    matriz = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ]
    resultado = escanear_estanteria_bodega(matriz, 0, 0)
    assert resultado == 3


def test_contar_esquina_inferior_derecha():
    matriz = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 1],
    ]
    resultado = escanear_estanteria_bodega(matriz, 2, 2)
    assert resultado == 4


def test_sin_unos_en_vecindad():
    matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    resultado = escanear_estanteria_bodega(matriz, 1, 1)
    assert resultado == 0


def test_limite_borde_derecho():
    matriz = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0],
    ]
    resultado = escanear_estanteria_bodega(matriz, 0, 2)
    assert resultado == 4


#Tests: calcular_descuento_cascada

def test_caso_base_porcentaje_final():
    nodo = {"porcentaje_final": 20}
    resultado = calcular_descuento_cascada(nodo)
    assert resultado == 20


def test_cliente_frecuente_va_derecha():
    nodo = {
        "cliente_frecuente": True,
        "derecha": {"porcentaje_final": 30},
        "izquierda": {"porcentaje_final": 10},
    }
    resultado = calcular_descuento_cascada(nodo)
    assert resultado == 30


def test_cliente_no_frecuente_va_izquierda():
    nodo = {
        "cliente_frecuente": False,
        "derecha": {"porcentaje_final": 30},
        "izquierda": {"porcentaje_final": 10},
    }
    resultado = calcular_descuento_cascada(nodo)
    assert resultado == 10


def test_recursion_multinivel():
    nodo = {
        "cliente_frecuente": True,
        "derecha": {
            "cliente_frecuente": False,
            "izquierda": {"porcentaje_final": 25},
            "derecha": {"porcentaje_final": 50},
        },
        "izquierda": {"porcentaje_final": 5},
    }
    resultado = calcular_descuento_cascada(nodo)
    assert resultado == 25


#Tests: ordenar_productos_quicksort

def test_ordenar_lista_desordenada():
    productos = [
        {"nombre": "C", "precio": 30},
        {"nombre": "A", "precio": 10},
        {"nombre": "B", "precio": 20},
    ]
    resultado = ordenar_productos_quicksort(productos)
    precios = [p["precio"] for p in resultado]
    assert precios == [10, 20, 30]


def test_ordenar_lista_vacia():
    resultado = ordenar_productos_quicksort([])
    assert resultado == []


def test_ordenar_un_elemento():
    productos = [{"nombre": "X", "precio": 99}]
    resultado = ordenar_productos_quicksort(productos)
    assert resultado[0]["precio"] == 99


def test_ordenar_precios_iguales():
    productos = [
        {"nombre": "A", "precio": 15},
        {"nombre": "B", "precio": 15},
    ]
    resultado = ordenar_productos_quicksort(productos)
    assert len(resultado) == 2
    assert resultado[0]["precio"] == 15


def test_ordenar_ya_ordenada():
    productos = [
        {"nombre": "A", "precio": 5},
        {"nombre": "B", "precio": 10},
        {"nombre": "C", "precio": 50},
    ]
    resultado = ordenar_productos_quicksort(productos)
    precios = [p["precio"] for p in resultado]
    assert precios == [5, 10, 50]


#Tests: buscar_precio_binario

def test_buscar_precio_existente():
    lista = [
        {"nombre": "A", "precio": 10},
        {"nombre": "B", "precio": 20},
        {"nombre": "C", "precio": 30},
    ]
    resultado = buscar_precio_binario(lista, 20)
    assert resultado == 1


def test_buscar_precio_no_existente():
    lista = [
        {"nombre": "A", "precio": 10},
        {"nombre": "B", "precio": 20},
        {"nombre": "C", "precio": 30},
    ]
    resultado = buscar_precio_binario(lista, 99)
    assert resultado == -1


def test_buscar_primer_elemento():
    lista = [
        {"nombre": "A", "precio": 5},
        {"nombre": "B", "precio": 15},
        {"nombre": "C", "precio": 25},
    ]
    resultado = buscar_precio_binario(lista, 5)
    assert resultado == 0


def test_buscar_ultimo_elemento():
    lista = [
        {"nombre": "A", "precio": 5},
        {"nombre": "B", "precio": 15},
        {"nombre": "C", "precio": 25},
    ]
    resultado = buscar_precio_binario(lista, 25)
    assert resultado == 2


def test_buscar_lista_vacia():
    resultado = buscar_precio_binario([], 10)
    assert resultado == -1