from tkinter import *
from tkinter import ttk

valoresCombustiveis = [6,4,7]
combustiveis = ["Gasolina","Etanol","Diesel"]
textoInicio = "                        BEM-VINDO         \nEscolha uma opção de combustivel"
camadas = "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯"
logo='limited development team JML².exe ᕦ(ò_óˇ)ᕤ'
root = Tk()
rBValue = IntVar()
rBValue.set(True)

root.title('Posto de Combustível JML²')
root.geometry('390x280')
root.resizable(False, False)
#logo = PhotoImage(file='logoPosto.png')
#logo = logo.subsample(2,2)

def inicio():
    inicioFrame = ttk.Frame(root,padding=5)
    inicioFrame.grid(column=0,row=2,sticky=(N,W,E,S))
    #figura1 = Label(logo).grid(column=0,row=0,pady=3)
    ttk.Label(inicioFrame,text=logo,font=('Georgia',12,'bold'),foreground='#ff6f00').grid(column=0,row=0,pady=3)
    ttk.Label(inicioFrame,text=textoInicio,font=('Georgia',12,'bold'),foreground='#ff6f00').grid(column=0,row=3,pady=15)
    ttk.Button(inicioFrame,text='Gasolina',command=lambda:intermediaria(0,inicio)).grid(column=0,row=4,padx=150)
    ttk.Button(inicioFrame,text='Etanol',command=lambda:intermediaria(1,inicio)).grid(column=0,row=5,padx=150)
    ttk.Button(inicioFrame,text='Diesel',command=lambda:intermediaria(2,inicio)).grid(column=0,row=6,padx=150)
    ttk.Button(inicioFrame,text='Sair',command=root.quit).grid(column=0,row=7,padx=150)
    ttk.Label(inicioFrame,text=camadas,font=('Georgia',12),foreground='#ff6f00').grid(column=0,row=8,pady=9)


formaPedido = ["Digite abaixo a quantidade em litros","Digite abaixo a quantidade em reais"]  
def intermediaria(comb,voltar):
    resultado = StringVar()
    textoPreEntry= StringVar()
    textoPreEntry.set(formaPedido[rBValue.get()-1])
    def troca():
        textoPreEntry.set(formaPedido[rBValue.get()-1])
    def calcular(qtd,f,comb,mdp):
        if f == 1:
            if mdp == 0:
                x=qtd*valoresCombustiveis[comb]
                resultado.set(f'R$ {x:,.2f} de {combustiveis[comb]}')
            elif mdp ==1:
                x=qtd*valoresCombustiveis[comb]
                x=x*1.08
                resultado.set(f'R$ {x:,.2f} de {combustiveis[comb]}')
        else:
            if mdp == 0:
                resultado.set(f'{str(qtd/valoresCombustiveis[comb])} L de {combustiveis[comb]}')
            elif mdp == 1:
                x=qtd/valoresCombustiveis[comb]
                x=x*0.92
                resultado.set(f'{str(x)} L de {combustiveis[comb]}')

    intermediariaFrame = ttk.Frame(root,padding=5)
    intermediariaFrame.grid(column = 0,row=2,sticky=(N,W,E,S))
    ttk.Label(intermediariaFrame,text=logo,font=('Georgia',12,'bold'),foreground='#ff6f00').grid(column=0,row=0)
    ttk.Label(intermediariaFrame,text="Método de Abastecimento",font=('Georgia',12,'bold'),foreground='#ff6f00').grid(column=0,row=1)
    
    rBL = Radiobutton(intermediariaFrame,text='Litros',var=rBValue,value=1, command=troca).grid(column=0,row=2,padx=150)
    
    rBR= Radiobutton(intermediariaFrame,text='Reais',var=rBValue,value=2,command=troca).grid(column=0,row=3,padx=150)
    labelResultado = ttk.Label(intermediariaFrame)
    ttk.Label(intermediariaFrame,textvariable=textoPreEntry).grid(column=0,row=4)
    qtd = ttk.Entry(intermediariaFrame)
    qtd.grid(column=0,row=5,padx=100,pady=5)

    ttk.Button(intermediariaFrame,text=' Calcular a vista ',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb,0)).grid(column=0,row=6)
    ttk.Button(intermediariaFrame,text='Calcular no cartão',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb,1)).grid(column=0,row=7)

    ttk.Label(intermediariaFrame,textvariable=resultado,font=('Courier',10),foreground='#ff6f00').grid(column=0,row=8) #
    ttk.Button(intermediariaFrame,text='Voltar',command=voltar).grid(column=0,row=10,padx=150)
inicio()

root.mainloop()

#'   _/﹋\_       _/﹋\_       _/﹋\_       _/﹋\_      ')
#'   (҂`_´)       (҂`_´)       (҂`_´)       (҂`_´)     ')
#'   <,︻╦╤─      <,︻╦╤─      <,︻╦╤─      <,︻╦╤─     ')
#'  _/﹋\_        _/﹋\_       _/﹋\_       _/﹋\_      ')
#' SR.JAIR.V    SR.MATHEUS.K SR.LUCAS.P    SR.LUCAS.M  ')
#'     limited development team JML.exe ᕦ(ò_óˇ)ᕤ      ')