fichas= ['o','x'] 

def generar_tablero(n, movimientos_jugadores): 

    tablero=[] 

    for i in range(n): 

        fila=['_' for i in range(n)] 

        for j in range(n): 

            casilla_vacia = True 

            for k in range(len(movimientos_jugadores)): 

                movimientos_jugador= movimientos_jugadores[k] 

 

                if i in movimientos_jugador: 

                    if j in movimientos_jugador[i]: 

                        fila[j]=fichas[k] 

        tablero.append(fila) 

    return tablero 

 
#n=3
#t= generar_tablero(n, movimientos_jugadores) 

#print(t, len(t)) 

#PASO 2
""" 
Método que comprueba que un movimiento de un jugador es válido 

    * x: fila donde el jugador quiere colocar la ficha. 

    * y: columna donde el jugador quiere colocar su ficha. 

    * movimientos_otro_jugador: listado con las celdas ocupadas por el otro jugador. 

""" 

def movimiento_valido(x, y, movimientos_otro_jugador, n): 

    if x > n or y > n: 

        return False 

    if x in movimientos_otro_jugador: 

        movimientos_en_columna= movimientos_otro_jugador[x] 

        if y in movimientos_en_columna: 

            return False 

    return True 
