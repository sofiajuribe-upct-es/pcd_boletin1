
import pytest
from juego_3_en_raya_bol2 import mostrar_tablero, movimiento_valido


#Los .fixture siempre se ponen en el archivo de test
@pytest.fixture #permite inyectar autimaticamente en los test qie las necesiten pasando su nombre como argumento
def tablero_dimension():
    return 3

#como daba error al intentar ejecutar, necesitamos añadir un nuevo fixture que cree los movimientos de ambos jugadores
@pytest.fixture
def movimientos_ambos_jugadores():
    movimientos_jugador_1 = {}
    movimientos_jugador_2 = {}
    return [movimientos_jugador_1, movimientos_jugador_2]


def test_mostrar_tablero(tablero_dimension, movimientos_ambos_jugadores, capsys):
    mostrar_tablero(tablero_dimension, movimientos_ambos_jugadores)
    captured = capsys.readouterr()
    lineas = captured.out.strip().split("\n")
    lineas= [l for l in lineas if l]
    assert len(lineas) == tablero_dimension
    for linea in lineas:
        assert len(linea.replace(' ', '')) == tablero_dimension

#PASO 2: aladimos fixtures
@pytest.fixture
def movimientos_vacios():
    return {}, {}

@pytest.fixture
def movimientos_ocupados():
    return {2:[3]}

@pytest.fixture
def movimientos_fuera_tablero(tablero_dimension):
    return tablero_dimension + 1, tablero_dimension + 1

def test_movimiento_columna_fuera_tablero(tablero_dimension, movimientos_vacios):
    movimientos_otro_jugador, _ = movimientos_vacios
    x = 1
    y = tablero_dimension + 1
    assert not movimiento_valido(tablero_dimension, x, y, movimientos_otro_jugador)

def test_movimiento_fila_y_columna_fuera_tablero(tablero_dimension, movimientos_vacios,
    movimientos_fuera_tablero):
    movimientos_otro_jugador, _ = movimientos_vacios
    x, y = movimientos_fuera_tablero
    assert not movimiento_valido(tablero_dimension, x, y, movimientos_otro_jugador)

def test_movimiento_incorrecto(tablero_dimension, movimientos_ocupados):
    x = 2
    y = 3
    assert not movimiento_valido(tablero_dimension, x, y, movimientos_ocupados)
 