import random


def HyperSudoku():
    tablero = [[0 for x in range(9)] for y in range(9)]
    cantidad = random.randint(7,20)
    modo = "hyper"
    # El range utilizado aquí es la cantidad de numeros que aparecen en el grid,con min 8 y max 20 numeros
    for i in range(cantidad):
        # Elegir numeros aleatorios
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while (not Validacion(tablero, row, col, num, modo) or tablero[row][col] != 0):  # Si ya está ocupado o no es valido, se corre de nuevo
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        tablero[row][col] = num


def Validacion(tablero, row, col, num, modo):
    """
    La función Validación se encarga de verificar si
    el dígito colocado en la posición definida,
    es correcto de acuerdo con las reglas del  juego

    Variables:
    Tablero: Grid inicial
    row: La fila
    col: La columna
    num: Número entre 1 y 9
    modo: hyper o diagonal

    Retorna:
    Si es válido o no


    """



    # verifica en la fila
    # verifica la columna y la fila
    for x in range(9):
        if tablero[x][col] == num:
            return False
        
    for y in range(9):
        if tablero[row][y] == num:
            return False
        
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # verifica si la sección es valida
            if (tablero[rowsection * 3 + x][colsection * 3 + y] == num):
                return False
    #Verifica los numeros en las diagonales
    if modo == "diagonal":
        if row-col == 0: #revisa diagonales de izquierda-arriba hasta derecha-abajo 
            for i in range (0,9):
                if tablero[i][i] == num: #Si el numero en la diagonal es igual a "num", se retorna False
                    return False
        if row+col == 8: #verifica si se está en la ultima posicion del tablero (inferior derecha)
            for i in range (0,9):
                if tablero[i][8-i] == num: #Revisa diagonales que van de izquierda-abajo hasta derecha-arriba
                    return False
                
    if modo == "hyper":
        if row != 0 and row != 4 and row != 8:
            if col != 0 and col != 4 and col != 8: #En estas dos lineas revisa que se esté usando las 4 regiones de HyperSudoku
                xr = row//4
                yr = col//4
                for i in range (1,4):
                    for j in range (1,4):
                        if tablero[(xr*4)+i][(yr*4)+j]==num: #Revisa que los numeros puestos sean validos
                            return False
                        
    return True


HyperSudoku()


