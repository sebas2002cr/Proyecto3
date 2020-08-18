import os
import os.path as p
import tkinter as tk
from tkinter.ttk import *
import random
from tkinter import *
import tkinter.messagebox as tkMsgBox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.tablero = []
        self.modi = []
        #self.restantes=81
        self.numero_selec = 0
        self.colores_n = ["#FFFFFF","#4D6F5C","#6FD199","#D1BA64","#85324A","#D15A7B","#D1790A","#2D4470","#178AD1","#772885"]
        self.colores_d = ["#000000","#001A40","#009988","#FFF6AE","#0096EB","#FFAD69","#83D5FF","#E3E3CF","#99000B","#949924"]
        self.colores="normal"
        self.modo=2

        self.HyperSudoku()



        print(self.tablero)
        #self.restantes-=self.modi.count(1)
        self.create_buttons()
        self.posibilidad = False
        #self.resolver()
        

    def Completo(self):
        """
        La funcion revisa las posiciones verificando que esten correctas

        Parametros:
        ninguno
        
        Retorna:
        False si algun color es incorrecto, True si odo esta correcto
        """
        
        for i in range (9):
            for j in range(9):
                if self.modi[i][j]==1: #Se salta las posiciones inmodificables
                    if not self.Validacion(i,j,self.tablero[i][j]) or self.tablero[i][j]==0:
                        return False
        return True

    def editar(self,botn,x,y):
        """
        La funcion cambia los valores de las casillas

        Parametros:
        botn:
        x:
        y:
        
        Retorna:
        nada
        """
        
        if self.colores=="normal":
            back=self.colores_n
        else:
            back=self.colores_d
        if self.modi[x][y] == 1:
            if self.posibilidad == True and self.numero_selec!=0:
                botn["anchor"]=self.posiciones[self.numero_selec-1]
                botn["text"]="▉"
                botn["fg"]=back[self.numero_selec]
            else:
                botn["bg"] = back[self.numero_selec]
                self.tablero[x][y]=self.numero_selec
                botn["text"]=""

    def cambiar(self):
        """
        La funcion cambia la variable que permite la insercion de colores pequeños en un campo

        Parametros:
        ninguno

        Retorna
        nada
        """
        
        if self.posibilidad == False:
            self.posibilidad = True
        else:
            self.posibilidad = False

    def create_buttons(self):
        """
        La funcion crea todos los botones necesarios para el juego

        Parametros:
        ninguno

        Retorna:
        nada
        """
        
        self.Botones = [[0 for x in range(9)] for y in range(9)]
        self.Seleccion = [0,0,0,0,0,0,0,0,0]

        #Se crean botones de seleccion:
        for u in range(9):
            self.create_selec(u)

        #se crean botones en la matriz del sudoku
        for ypos in range(9):
            for xpos in range(9):
                self.create_espacios(ypos*55+20,xpos*55+45,self.tablero[ypos][xpos],ypos,xpos)
                
        #Boton para salir, este guarda la partida y sale        
        self.quit = tk.Button(text="Salir", fg="red",bg="black")
        self.quit.pack()
        self.quit.place(bordermode=OUTSIDE,height=30, width=50, x=255,y=620)
        
        

                    
        #Boton para eliminar un color puesto
        self.elim = tk.Button(text="Eliminar",command= lambda:self.introducir(0))
        self.elim.pack()
        self.elim.place(bordermode=INSIDE,height=30,width=60,x=200,y=620)

        
              

    def introducir(self,i):
        """
        La funcion cambia el valor de la funcion por el nuevo valor

        Parametros:
        i: el numero de iteracion correspondiente al boton de seleccion(de 1 a 9)

        Retorna:
        nada
        """
        
        self.numero_selec = i
        
    def create_selec(self,u):
            if self.colores=="normal":
                back=self.colores_n
            else:
                back=self.colores_d
            self.boton_selec = tk.Button(text=u+1, fg="white",bg=back[u+1],command= lambda:self.introducir(u+1))
            self.boton_selec.pack()
            self.boton_selec.place(bordermode=OUTSIDE,height=47, width=47, x=(u+1)*50+6,y=550)
            self.Seleccion[u]=int(self.boton_selec["text"])

    def create_espacios(self,ypos,xpos,color,x,y):
        """
        La funcion crea los botones(los 81) con sus correspondientes colores(de 0 a 9)

        Parametros:
        xpos: la posicion x en la interfaz
        ypos: la posicion y en la interfaz
        color: el numero(color) que esta en la posicion x,y del tablero(sudoku)
        x: posicion x del tablero
        y: posicion y del tablero

        Retorna:
        nada
        """
        
        if self.colores=="normal":
            self.boton = tk.Button(bg=self.colores_n[color], command= lambda:self.editar(self.Botones[x][y],x,y))
        else:
            self.boton = tk.Button(bg=self.colores_d[color], command= lambda:self.editar(self.Botones[x][y],x,y))
        self.boton.pack()
        self.boton.place(bordermode=OUTSIDE, height=47, width=47,x=xpos,y=ypos)
        self.Botones[x][y]=self.boton #Añade el boton a una lista de botones, para poder manejar cada uno
        
    def HyperSudoku(self):
        self.tablero = [[0 for x in range(9)] for y in range(9)]#todos los espacios se crean con 0
        self.modi = [[1 for x in range(9)]for y in range(9)]#todos los espacios son modificables
        self.cantidad = random.randint(8,20)
        # El range utilizado aquí es la cantidad de numeros que aparecen en el grid,con min 8 y max 20 numeros
        for i in range(self.cantidad):
            # Elegir numeros aleatorios
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
            while (not self.Validacion(row, col, num) or self.tablero[row][col] != 0):  # Si ya está ocupado o no es valido, se corre de nuevo
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            self.tablero[row][col] = num #este espacio se cambia por el num
            self.modi[row][col] = 0 #este espacio no va a ser modificable
            


        
    def Validacion(self, y, x, num):
        """
        La funcion verifica si un color se puede ingresar en la posicion x,y

        Parametros:
        row: posicion x del tablero
        col: posicion y del tablero
        num: numero(color) a ingresar
        
        Retorna False si no se puede ingresar, True cuando si se pueda
        """
        #Verifica los numeros en las 4 secciones adicionales            
        if self.modo == 2:
            if x != 0 and x != 4 and x != 8:
                if y != 0 and y != 4 and y != 8: #En estas dos lineas revisa que se esté usando las 4 regiones de HyperSudoku
                    xr = x//4
                    yr = y//4
                    for i in range (1,4):
                        for j in range (1,4):
                            if self.tablero[(yr*4)+i][(xr*4)+j]==num: #Revisa que los numeros puestos sean validos dentro de la seccion
                                self.num_posible=str((yr*4)+i)+str((xr*4)+j)
                                return False
        # verifica la columna y la fila
        for i in range(9):
            if self.tablero[i][x] == num:
                self.num_posible=str(i)+str(x)
                return False
            
        for i in range(9):
            if self.tablero[y][i] == num:
                self.num_posible=str(y)+str(i)
                return False
            
        xsection = x//3*3
        ysection = y//3*3
        for i in range(3):
            for j in range(3):
                # verifica si la sección es valida
                if (self.tablero[ysection+ i][xsection + j] == num):
                    lay=ysection+i
                    lax=xsection+j
                    self.num_posible=str(lay)+str(lax)
                    return False
        #Verifica los numeros en las diagonales
        if self.modo == 1:
            if x-y == 0: #revisa diagonal de esquina superior izquierda hasta la inferior derecha 
                for i in range (0,9):
                    if self.tablero[i][i] == num: #Si el numero en la diagonal es igual a "num", se retorna False
                        self.num_posible=str(i)+str(i)
                        return False
            if x+y == 8: #revisa diagonal de esquina inferior izquierda hasta la superior derecha
                for i in range (0,9):
                    if self.tablero[8-i][i] == num: #Revisa diagonales que van de izquierda-abajo hasta derecha-arriba
                        self.num_posible=str(8-1)+str(i)
                        return False
                            
        return True



root = tk.Tk()
app = Application(master=root)
root.title("Sudoku")
root.geometry("580x650")
root.configure(bg="#FFFFFF")
app.mainloop()
