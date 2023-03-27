from tkinter import *
from tkinter import ttk

valoresCombustiveis = [6.0, 4.0, 5.5]
combustiveis = ["Gasolina", "Etanol", "Diesel"]
textoInicio = "========BEM-VINDO========\nEscolha uma opção de combustivel:"

# root = Tk()
# rBValue = IntVar()
# rBValue.set(True)

# root.title('Combustiveis')
# root.geometry('500x300')

AppPosto = Tk()
AppPosto.title("Posto do Arca de nóe")
AppPosto.geometry("600x600")
AppPosto.resizable(width=False, height=False)
AppPosto.configure(background="blue")

rBValue = IntVar()
rBValue.set(True)


def inicio():
    inicioFrame = ttk.Frame(AppPosto, padding=5)
    inicioFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ttk.Label(inicioFrame, text=textoInicio).grid(column=0, row=0, pady=20)
    ttk.Button(inicioFrame, text='Gasolina', command=lambda: intermediaria(0, inicio)).grid(column=0, row=1, pady=10)
    ttk.Button(inicioFrame, text='Etanol', command=lambda: intermediaria(1, inicio)).grid(column=0, row=2, pady=10)
    ttk.Button(inicioFrame, text='Diesel', command=lambda: intermediaria(2, inicio)).grid(column=0, row=3, pady=10)
    ttk.Button(inicioFrame, text='Sair', command=AppPosto.quit).grid(column=0, row=4, pady=10)


formaPedido = ["Qtd de Litros", "R$ "]

def mododepagamento():
    ttk.Label(mododepagamento,text="====Litro ou Real?====").grid(column=0, row=8, pady=10)
def intermediaria(comb,voltar):
    resultado = StringVar()
    textoPreEntry= StringVar()
    textoPreEntry.set(formaPedido[rBValue.get()-1])
    def troca():
        textoPreEntry.set(formaPedido[rBValue.get()-1])
    def calcular(qtd,f,comb):
        if f == 1:
            x=qtd*valoresCombustiveis[comb]
            resultado.set(f'R$ {x:,.2f} de {combustiveis[comb]}')
        else:
            resultado.set(f'{str(qtd/valoresCombustiveis[comb])} L de {combustiveis[comb]}')

    intermediariaFrame = ttk.Frame(AppPosto,padding=5)
    intermediariaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ttk.Label(intermediariaFrame,text="====Litro ou Real?====").grid(column=0, row=0, pady=10)
    rBL = Radiobutton(intermediariaFrame,text='Litro',var=rBValue,value=1, command=troca).grid(column=0, row=2, pady=10)
    rBR= Radiobutton(intermediariaFrame,text='Real',var=rBValue,value=2,command=troca).grid(column=0, row=3, pady=10)
    labelResultado = ttk.Label(intermediariaFrame)
    ttk.Label(intermediariaFrame,textvariable=textoPreEntry).grid(column=0, row=4, pady=10)
    qtd = ttk.Entry(intermediariaFrame)
    ttk.Label(intermediariaFrame,textvariable=resultado).grid(column=1, row=4, pady=10)
    qtd.grid(column=0, row=5, pady=10)
    ttk.Button(intermediariaFrame,text='Calcular',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb)).grid(column=1, row=5, pady=10)
    ttk.Button(intermediariaFrame,text='Voltar',command=voltar).grid(column=0, row=6, pady=10)
    ttk.Button(intermediariaFrame,text='Pagar',command=lambda : mododepagamento()).grid(column=1, row=6, pady=10)
inicio()

AppPosto.mainloop()