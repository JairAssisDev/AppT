from tkinter import *
from tkinter import ttk

valoresCombustiveis = [6,4,7]
combustiveis = ["Gasolina","Etanol","Diesel"]
textoInicio = "                       BEM-VINDO         \nEscolha uma opção de combustivel"
camadas = "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯"

root = Tk()
rBValue = IntVar()

root.title('Posto de Combustível JML²')
root.geometry('390x450')
root.resizable(False, False)
logo = PhotoImage(file='logoPosto.png')
logo = logo.subsample(2,2)

def inicio():
    inicioFrame = ttk.Frame(root,padding=5)
    inicioFrame.grid(column=0,row=2,sticky=(N,W,E,S)) # type: ignore
    figura1 = Label(image=logo).grid(column=0,row=0,pady=3)
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
    textoPreEntry.set(formaPedido[rBValue.get()])
    def troca():
        textoPreEntry.set(formaPedido[rBValue.get()])
    def calcular(qtd,f,comb,mdp):
        if f == 1:
            if mdp == 0:
                x=qtd*valoresCombustiveis[comb]
                resultado.set(f'R${x:,.2f} de {combustiveis[comb]}')
            elif mdp ==1:
                x=qtd*valoresCombustiveis[comb]
                x=x*1.08
                resultado.set(f'R${x:,.2f} de {combustiveis[comb]}')
        else:
            if mdp == 0:
                resultado.set(f'{str(round(qtd/valoresCombustiveis[comb],2))}L de {combustiveis[comb]}')
            elif mdp == 1:
                x=qtd/valoresCombustiveis[comb]
                x=x*0.92
                resultado.set(f'{str(round(x,2))}L de {combustiveis[comb]}')

    intermediariaFrame = ttk.Frame(root,padding=5)
    intermediariaFrame.grid(column = 0,row=2,sticky=(N,W,E,S)) # type: ignore
    ttk.Label(intermediariaFrame,text="Método de Abastecimento",font=('Georgia',12,'bold'),foreground='#ff6f00').grid(column=0,row=0)
    
    rBL = Radiobutton(intermediariaFrame,text='Litros',var=rBValue,value=0, command=troca).grid(column=0,row=1,padx=150) # type: ignore
    
    rBR= Radiobutton(intermediariaFrame,text='Reais',var=rBValue,value=1,command=troca).grid(column=0,row=2,padx=150) # type: ignore
    labelResultado = ttk.Label(intermediariaFrame)
    ttk.Label(intermediariaFrame,textvariable=textoPreEntry).grid(column=0,row=3)
    qtd = ttk.Entry(intermediariaFrame)
    qtd.grid(column=0,row=4,padx=100,pady=5)
    ttk.Button(intermediariaFrame,text='Calcular a vista',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb,0)).grid(column=0,row=5)
    ttk.Button(intermediariaFrame,text='Calcular no cartão',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb,1)).grid(column=0,row=6)
    ttk.Label(intermediariaFrame,textvariable=resultado,font=('Courier',10),foreground='#ff6f00').grid(column=0,row=7)
    ttk.Button(intermediariaFrame,text='Voltar',command=voltar).grid(column=0,row=10,padx=150)
inicio()

root.mainloop()