import pytest
from juego_3_en_raya import generar_tablero, movimiento_valido

def test_generar_tablero():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores = [mov_jugador_1, mov_jugador_2]
    n = 3

    t = generar_tablero(n, movimientos_jugadores)

    assert len(t) == n
    for fila in t:
        assert len(fila) == n

#PASO 2
def test_movimiento_columna_fuera_tablero(): 

    movimientos_otro_jugador={} 
    n=3
    x=  1 

    y=  n+1 

    assert False == movimiento_valido(x,y,movimientos_otro_jugador, n) 

 

def test_movimiento_fila_y_columna_fuera_tablero(): 

    movimientos_otro_jugador={} 
    n=3
    x=  n+1 

    y=  n+1 

    assert False == movimiento_valido(x,y,movimientos_otro_jugador, n) 

 

def test_movimiento_incorrecto(): 

    movimientos_otro_jugador={2:[3]} 
    n=3
    x=  2 

    y=  3 

    assert False == movimiento_valido(x,y,movimientos_otro_jugador, n) 
