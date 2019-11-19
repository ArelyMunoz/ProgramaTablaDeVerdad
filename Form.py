from Tkinter import *

app = Tk()
app.geometry("560x80")
app.title("Programa calcular tabla de verdad")
app.configure(background="dodgerblue")

VarP = False
VarQ = False
VarR = False
Resultado = StringVar()

def Conjuncion():
    if SpbP.get() == "1" and SpbQ.get() == "1":
        Resultado.set("Verdadero")
    elif SpbP.get() == "1" and SpbQ.get() == "0":
        Resultado.set("Falso")
    elif SpbP.get() == "0" and SpbQ.get() == "1":
        Resultado.set("Falso")
    elif SpbP.get() == "0" and SpbQ.get() == "0":
        Resultado.set("Falso")

def Disyucion():
    if SpbP.get() == "1" and SpbQ.get() == "1":
        Resultado.set("Verdadero")
    elif SpbP.get() == "1" and SpbQ.get() == "0":
        Resultado.set("Verdadero")
    elif SpbP.get() == "0" and SpbQ.get() == "1":
        Resultado.set("Verdadero")
    elif SpbP.get() == "0" and SpbQ.get() == "0":
        Resultado.set("Falso")

def Condicional():
    if SpbP.get() == "1" and SpbQ.get() == "1":
        Resultado.set("Verdadero")
    elif SpbP.get() == "1" and SpbQ.get() == "0":
        Resultado.set("Falso")
    elif SpbP.get() == "0" and SpbQ.get() == "1":
        Resultado.set("Verdadero")
    elif SpbP.get() == "0" and SpbQ.get() == "0":
        Resultado.set("Verdadero")

def Bidicional():
    if SpbP.get() == "1" and SpbQ.get() == "1":
        Resultado.set("Verdadero")
    elif SpbP.get() == "1" and SpbQ.get() == "0":
        Resultado.set("Falso")
    elif SpbP.get() == "0" and SpbQ.get() == "1":
        Resultado.set("Falso")
    elif SpbP.get() == "0" and SpbQ.get() == "0":
        Resultado.set("Verdadero")

FrameTV = Frame(app, width = 560, height = 80)
FrameTV.pack()

FrameTV.configure(background="dodgerblue")

LblP = Label(FrameTV, text = "P", bg="skyblue", width = 7)
LblP.grid(row = 0, column = 0)

LblQ = Label(FrameTV, text = "Q", bg="skyblue", width = 7)
LblQ.grid(row = 0, column = 1)

LblS = Label(FrameTV, text = "Opcion", bg="skyblue", width = 20)
LblS.grid(row = 0, column = 2, columnspan = 4)

LblR = Label(FrameTV, text = "Resultado", bg="skyblue", width = 13)
LblR.grid(row = 0, column = 6)

SpbP = Spinbox(FrameTV, from_ = 0, to = 1, width = 4)
SpbP.grid(row = 1, column = 0)

SpbQ = Spinbox(FrameTV, from_ = 0, to = 1, width = 4)
SpbQ.grid(row = 1, column = 1)

BtnC = Button(FrameTV, text = "^", command = Conjuncion, width = 2)
BtnC.grid(row = 1, column = 2)

BtnD = Button(FrameTV, text = "v", command = Disyucion, width = 2)
BtnD.grid(row = 1, column = 3)

BtnCN = Button(FrameTV, text = "->", command = Condicional, width = 2)
BtnCN.grid(row = 1, column = 4)

BtnB = Button(FrameTV, text = "<->", command = Bidicional, width = 2)
BtnB.grid(row = 1, column = 5)

LblRes = Label(FrameTV, textvariable = Resultado, bg="dodgerblue", width = 10)
LblRes.grid(row = 1, column = 6)

app.mainloop()