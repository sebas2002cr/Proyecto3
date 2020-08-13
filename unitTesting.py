from TableroInicial import*
def test_HyperSudoku():
    assert HyperSudoku(tablero)
    assert row == 4
    assert col == 5
    assert num ==3

def test_validacion():
    assert Validacion(tablero, 1, 3, 7, "Hyper")== True
    assert Validacion(tablero , 5,6,"diagonal")== False
    assert tablero[2][6]==5
    assert tablero[1 * 3 + 5][2 * 3 + 4] == 6

def test_Validacion_modos():
    assert modo=="hype"
    assert modo=="diagonal"
    




