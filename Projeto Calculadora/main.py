from tkinter import *
import ctypes

#Variaveis globais
numvisor = ""
numhist = ""

#Funções:
#Recebe os valores e sinais e armazena em numvisor
def mathexp(num):
    global numvisor
    numvisor += num
    matematica.set(numvisor)

#Limpa a area que aparace os calculos
def clear():
    global numvisor
    numvisor = ""
    matematica.set(numvisor)

#Realiza a operação matematica
def mathdo():
    global numvisor
    global numhist
    try:
        matematica.set(str(eval(numvisor)))
        numhist += numvisor+": "+str(eval(numvisor))+"\n"
        matematicahist.set(numhist)
        numvisor=""
    except SyntaxError:
        numvisor=""
        matematica.set("Invalid syntax")
    except ZeroDivisionError:
        numvisor = ""
        matematica.set("Cannot divide by zero")

#Criando janela
window = Tk()
window.title("Calculadora")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

#Variaveis do programa
matematica = StringVar()
matematica.set("")
matematicahist = StringVar()
padx = 5

#Area que aparace os calculos
visor = Label(window,
              textvariable=matematica,
              font=('Newake',15),
              bg='white',
              width=24,
              height=5).grid(row=0,column=0,columnspan=3)

#Historico de calculos
visorhist = Label(window,
              textvariable=matematicahist,
              wraplength=180,
              font=('Newake',10),
              bg='white',
              width=10,
              border=1,
              relief="sunken",
              height=7).grid(row=0,column=3,columnspan=4)

#Criando botões numericos de 0-9
num1 = Button(window,
              text="1",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("1")).grid(row=3,column=0)
num2 = Button(window,
              text="2",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("2")).grid(row=3,column=1)
num3 = Button(window,
              text="3",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("3")).grid(row=3,column=2)
num4 = Button(window,
              text="4",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("4")).grid(row=2,column=0)
num5 = Button(window,
              text="5",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("5")).grid(row=2,column=1)
num6 = Button(window,
              text="6",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("6")).grid(row=2,column=2)
num7 = Button(window,
              text="7",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("7")).grid(row=1,column=0)
num8 = Button(window,
              text="8",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("8")).grid(row=1,column=1)
num9 = Button(window,
              text="9",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("9")).grid(row=1,column=2)
num0 = Button(window,
              text="0",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=lambda: mathexp("0")).grid(row=4,column=1)

#Botões de operação matematica
add = Button(window,
              text="+",
              font=('Newake',20),
              bg='white',
              width=5,
              command=lambda: mathexp("+")).grid(row=4,column=3)
subtract = Button(window,
              text="-",
              font=('Newake',20),
              bg='white',
              width=5,
              command=lambda: mathexp("-")).grid(row=3,column=3)
multiply = Button(window,
              text="x",
              font=('Newake',20),
              bg='white',
              width=5,
              command=lambda: mathexp("*")).grid(row=2,column=3)
divide = Button(window,
              text="/",
              font=('Newake',20),
              bg='white',
              width=5,
              command=lambda: mathexp("/")).grid(row=1,column=3)
equal = Button(window,
              text="=",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=mathdo).grid(row=4,column=2)
clear = Button(window,
              text="C",
              font=('Newake',20),
              bg='white',
              width=padx,
              command=clear).grid(row=4,column=0)

window.mainloop()