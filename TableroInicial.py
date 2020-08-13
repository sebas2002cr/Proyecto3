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
    
    if modo == "diagonal":
        if row-col == 0:
            for i in range (0,9):
                if tablero[i][i] == num:
                    return False
        if row+col == 8:
            for i in range (0,9):
                if tablero[i][8-i] == num:
                    return False
                
    if modo == "hyper":
        if row != 0 and row != 4 and row != 8:
            if col != 0 and col != 4 and col != 8:
                xr = row//4
                yr = col//4
                for i in range (1,4):
                    for j in range (1,4):
                        if tablero[(xr*4)+i][(yr*4)+j]==num:
                            return False
                        
    return True


HyperSudoku()


