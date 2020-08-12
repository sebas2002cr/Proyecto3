import random


def HyperSudoku():
    tablero = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            tablero[i][j] = 0

    # El range utilizado aquí es la cantidad de numeros que aparecen en el grid,con min 8 y max 20 numeros
    for i in range(8,20):
        # Elegir numeros aleatorios
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while (not Validación(tablero, row, col, num) or tablero[row][col] != 0):  # Si ya está ocupado o no es valido, se corre de nuevo
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        tablero[row][col] = num;

    Printgrid(tablero)


def Printgrid(tablero):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y == 6):
                print("|", end=" ")
            print(" " + str(tablero[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)


def Validación(tablero, row, col, num):
    # verifica en la fila
    valid = True
    # verifica la columna y la fila
    for x in range(9):
        if (tablero[x][col] == num):
            valid = False
    for y in range(9):
        if (tablero[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # verifica si la sección es valida
            if (tablero[rowsection * 3 + x][colsection * 3 + y] == num):
                valid = False
    return valid


HyperSudoku()


