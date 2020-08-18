import os
import os.path as p
import tkinter as tk
from tkinter.ttk import *
import random
from tkinter import *
import tkinter.messagebox as tkMsgBox
########################################################################2
class OtherFrame(tk.Toplevel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        tk.Toplevel.__init__(self)
        self.geometry("580x650")
        self.title("SUDOKU")
        self.tablero = []
        self.modi = []
        self.modo = self.original_frame.var.get()
        self.colores = self.original_frame.check.get()

        self.restantes=81
        self.numero_selec = 0
        self.colores_n = ["#FFFFFF","#4D6F5C","#6FD199","#D1BA64","#85324A","#D15A7B","#D1790A","#2D4470","#178AD1","#772885"]
        self.colores_d = ["#FFFFFF","#001A40","#CCFF00","#FFF6AE","#0096EB","#FFAD69","#83D5FF","#E3E3CF","#B0AD02","#949924"]
        self.posiciones = ["se","s","sw","e","center","w","ne","n","nw"]
        self.resumir=False
        if self.original_frame.res_g:
            self.arch("abrir")
        else:
            self.HyperSudoku()
            self.Corregir()
            self.reiniciar()
            self.Corregir()
            self.reiniciar()
        for e in range(9):
            self.restantes-=self.modi[e].count(0)
        self.create_buttons()
        self.posibilidad = False
        self.reiniciar()

#----------------------------------------------------------------------        
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
        
        if self.colores==0:
            back=self.colores_n
        else:
            back=self.colores_d
        if self.modi[x][y] == 1:
            if self.posibilidad == True and self.numero_selec!=0:
                botn["anchor"]=self.posiciones[self.numero_selec-1]
                botn["text"]="▉"
                botn["padx"]=2
                botn["fg"]=back[self.numero_selec]
            else:
                botn["bg"] = back[self.numero_selec]
                self.tablero[x][y]=self.numero_selec
                botn["text"]=""
                if self.numero_selec==0:
                    self.restantes+=1
                else:
                    self.restantes-=1
                if self.restantes==0:
                    if self.Completo():
                        self.Mensaje()

    #----------------------------------------------------------------------
    def Revisar(self):
        for i in range(9):
            for j in range(9):
                if self.modi[i][j]==1 and self.tablero[i][j]!=0:
                    if self.Validacion(i,j,self.tablero[i][j])==True:
                        self.rev2["text"]="Correcto"
                        
                    else:
                        self.rev2["text"]="Incorrecto"

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
    #----------------------------------------------------------------------
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
    #----------------------------------------------------------------------
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
        self.quit = tk.Button(self,text="Salir", fg="black",bg="beige",command=lambda:self.onClose())
        self.quit.pack()
        self.quit.place(bordermode=OUTSIDE,height=30, width=50, x=450,y=620)
        
        #Boton para activar la colocacion de posibles colores
        self.edi = tk.Button(self,text="Editar",fg="black",bg="beige",command=lambda:self.cambiar())
        self.edi.pack()
        self.edi.place(bordermode=OUTSIDE,height=30,width=50,x=290,y=620)

        #Boton para revisar si lo que se ha puesto es correcto
        self.revi = tk.Button(self,text="Revisar",fg="black",bg="beige",command=lambda:self.Revisar())
        self.revi.pack()
        self.revi.place(bordermode=OUTSIDE,height=30,width=50,x=230,y=620)
        self.rev2=tk.Label(self,text="",fg="black")
        self.rev2.pack()
        self.rev2.place(x=230,y=600)
        #Se crean las divisiones de cada seccion
        for i in range(1,3):
            self.linea = tk.Button(self,bg="black",state=tk.DISABLED)
            self.linea.pack()
            self.linea.place(height=500, width=3, x=165*i+39,y=15)
        for j in range(1,3):
            self.linea = tk.Button(self,bg="black",state=tk.DISABLED)
            self.linea.pack()
            self.linea.place(height=3, width=500,x=39,y=165*j+14)
        if self.modo == 2:
            for i in range(2):
                for j in range(2):
                    self.cuadrado = tk.Label(self,bg="grey")
                    self.cuadrado.pack()
                    self.cuadrado.place(height=167, width=167,x=i*220+95,y=j*220+70)
                    self.cuadrado.lower()
                    
        #Boton para eliminar un color puesto
        self.elim = tk.Button(self,text="Eliminar",bg="beige",command= lambda:self.introducir(0))
        self.elim.pack()
        self.elim.place(bordermode=INSIDE,height=30,width=60,x=155,y=620)
        #Boton para reiniciar la partida
        self.re = tk.Button(self,text="Reiniciar",bg="beige",command=lambda:self.reiniciar())
        self.re.pack()
        self.re.place(bordermode=INSIDE,height=30,width=60,x=350,y=620)
        
    #----------------------------------------------------------------------          
    def reiniciar(self):
        """
        La funcion reinicia el juego con la configuracion inicial

        Parametros:
        ninguno

        Retorna:
        nada
        """
        
        for x in range(9):
            for y in range(9):
                if self.modi[x][y] == 1: #Verficia si esa posicion es modificable
                    self.tablero[x][y]=0 #si lo es, su valor se reinicia a 0 
        self.numero_selec=0 #limpia la variable de colores de seleccion
        self.arch("guardar") #guarda el juego con la configuracion inicial en un archivo
        self.resumir=True
        self.restantes=81
        self.posibilidad=False
        self.tablero=[] #Limpia la lista de numeros en la matriz y la lista de modificables
        self.modi=[] #ya que nuevos datos se van a introducir en ellas(los de la configuracion inicial)
        self.arch("abrir")
        for i in range(9):
            for e in self.tablero[i]:
                if e!=0:
                    self.restantes-=1
        self.create_buttons()
    #----------------------------------------------------------------------    
    def introducir(self,i):
        """
        La funcion cambia el valor de la funcion por el nuevo valor

        Parametros:
        i: el numero de iteracion correspondiente al boton de seleccion(de 1 a 9)

        Retorna:
        nada
        """
        
        self.numero_selec = i
    #----------------------------------------------------------------------    
    def create_selec(self,u):
            if self.colores==0:
                back=self.colores_n
            else:
                back=self.colores_d
            self.boton_selec = tk.Button(self,text=u+1, fg="grey",bg=back[u+1],command= lambda:self.introducir(u+1))
            self.boton_selec.pack()
            self.boton_selec.place(bordermode=OUTSIDE,height=47, width=47, x=(u+1)*50+6,y=550)
            self.Seleccion[u]=int(self.boton_selec["text"])
    #----------------------------------------------------------------------
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
        
        if self.colores==0:
            self.boton = tk.Button(self,bg=self.colores_n[color], command= lambda:self.editar(self.Botones[x][y],x,y))
        else:
            self.boton = tk.Button(self,bg=self.colores_d[color], command= lambda:self.editar(self.Botones[x][y],x,y))
        self.boton.pack()
        self.boton.place(bordermode=OUTSIDE, height=47, width=47,x=xpos,y=ypos)
        self.Botones[x][y]=self.boton #Añade el boton a una lista de botones, para poder manejar cada uno
    #----------------------------------------------------------------------    
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
    #----------------------------------------------------------------------       
    def Corregir(self):
        for i in range (9):
            for j in range(9):
                if self.tablero[i][j]==0 or self.modi[i][j]==1:
                    self.tablero[i][j]=self.Posibilidad(i,j)
    #----------------------------------------------------------------------
    def Posibilidad(self,x,y):
        self.num_posible=""
        for num in range (1,10):
            if self.Validacion(x,y,num):
                return num
            else:
                numero=num
        self.tablero[int(self.num_posible[0])][int(self.num_posible[1])]=0
        self.modi[int(self.num_posible[0])][int(self.num_posible[1])]=1
        return 0
    #----------------------------------------------------------------------    
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

    #def Mrev(self,c):
        self.Mensaje=tkMsgBox.showinfo("Revision",f"{c}")
        #if self.Mensaje == "ok":
            
    #def Mensaje(self):
        Mensaje=tkMsgBox.showinfo("Terminado","¡Sudoku completado!")
    #----------------------------------------------------------------------
    def arch(self,accion):
        if accion == "guardar":
            archivo = open("resumir.txt","w+")
            for y in range(9):
                for x in range(9):
                    archivo.write(f"{self.tablero[y][x]},{self.modi[y][x]}\n")
            archivo.close()

        if accion == "abrir":
            if p.exists("resumir.txt"):
                archivo=open("resumir.txt","r")
                elem=archivo.readlines()
                lista1=[]
                lista2=[]
                con=1
                for e in elem:
                    lista1.append(int(e[0]))
                    lista2.append(int(e[2]))
                    con+=1
                    if con == 10:
                        self.tablero.append(lista1)
                        self.modi.append(lista2)
                        con = 1
                        lista1=[]
                        lista2=[]
            archivo.close()    
        if accion =="eliminar":
            os.remove("resumir.txt")
    #----------------------------------------------------------------------        
    def resolver(self):
        matriz=self.tablero.copy()
        for y in range(9):
            for x in range(9):
                if matriz[y][x]==0:
                    for n in range(1,10):
                        if self.Validacion(y,x,n):
                            matriz[y][x]=n
                            self.resolver()
                            matriz[y][x]=0
                    return     
        
    #----------------------------------------------------------------------
    def onClose(self):
        """"""
        #if tkMsgBox.askyesno(mesage="¿Desea salir?\nSu partida se guardara",title="Salir y Guardar")==True:
        self.arch("guardar")
        self.destroy()
        self.original_frame.show()
    
    #----------------------------------------------------------------------


########################################################################1
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Menu")
        self.frame = tk.Frame(parent)
        self.frame.pack()
                
        self.btn = tk.Button( text="Nuevo Juego",bg="beige", command=self.openFrame)
        self.btn.pack()
        self.btn.place(x=150,y=30)
        #self.btn.place(x=120,y=70)
        self.root["bg"] = "coral"
        self.var = tk.IntVar()
        self.R1 = tk.Radiobutton(root, text="X-Sudoku",bg="coral",variable = self.var,  value=1)
        self.R1.pack()
        self.R1.place(x=95,y=200)
        self.R2 = tk.Radiobutton(root, text="Hyper-Sudoku",bg="coral", variable = self.var, value=2)
        self.R2.pack()
        self.R2.invoke()
        self.R2.place(x=200,y=200)

        self.check = tk.IntVar()
        self.Check = tk.Checkbutton(root, text = "Daltonismo",bg="coral", variable = self.check,
                                    onvalue = 1, offvalue = 0, height=1, width = 10)
        self.Check.pack()
        self.Check.place(x=90,y=250)
        self.res_g = False
        if p.exists("prueba.txt"): #Verifica si hay algun archivo
            self.resumir = tk.Button( text="Resumir Juego",bg="beige",command=self.openFrame2)
            self.resumir.pack()
            self.resumir.place(x=150,y=90)
        
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
        
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        subFrame = OtherFrame(self)
    def openFrame2(self):
        self.res_g = True
        self.hide()
        subFrame = OtherFrame(self)
        
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("380x300")
    app = MyApp(root)
    root.mainloop()

