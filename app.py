from tkinter import *
from tkinter import ttk
valoresCombustiveis = [6,4,7]
combustiveis = ["Gasolina","Etanol","Diesel"]
textoInicio = "=======BEM-VINDO=======\nEscolha uma opção de combustivel:"

root = Tk()
rBValue = IntVar()
rBValue.set(True)

root.title('Combustiveis')
root.geometry('500x300')
def inicio():
    inicioFrame = ttk.Frame(root,padding=5)
    inicioFrame.grid(column = 0,row=0,sticky=(N,W,E,S))
    ttk.Label(inicioFrame,text=textoInicio).grid(column=0,row=0,pady=20)
    ttk.Button(inicioFrame,text='Gasolina',command=lambda:intermediaria(0,inicio)).grid(column=0,row=1,padx=150)
    ttk.Button(inicioFrame,text='Etanol',command=lambda:intermediaria(1,inicio)).grid(column=0,row=2,padx=150)
    ttk.Button(inicioFrame,text='Diesel',command=lambda:intermediaria(2,inicio)).grid(column=0,row=3,padx=150)
    ttk.Button(inicioFrame,text='Sair',command=root.quit).grid(column=0,row=4,padx=150)


formaPedido = ["Qtd de Litros","R$ "]  
def intermediaria(comb,voltar):
    resultado = StringVar()
    textoPreEntry= StringVar()
    textoPreEntry.set(formaPedido[rBValue.get()-1])
    def troca():
        textoPreEntry.set(formaPedido[rBValue.get()-1])
    def calcular(qtd,f,comb):
        if f == 1:
            resultado.set(f'R$ {str(qtd*valoresCombustiveis[comb])} de {combustiveis[comb]}')
        else:
            resultado.set(f'{str(qtd/valoresCombustiveis[comb])} L de {combustiveis[comb]}')

    intermediariaFrame = ttk.Frame(root,padding=5)
    intermediariaFrame.grid(column = 0,row=0,sticky=(N,W,E,S))
    ttk.Label(intermediariaFrame,text="Litro ou Real? ").grid(column=0,row=0)
    
    rBL = Radiobutton(intermediariaFrame,text='Litro',var=rBValue,value=1, command=troca).grid(column=0,row=1,padx=150)
    
    rBR= Radiobutton(intermediariaFrame,text='Real',var=rBValue,value=2,command=troca).grid(column=0,row=2,padx=150)
    labelResultado = ttk.Label(intermediariaFrame)
    ttk.Label(intermediariaFrame,textvariable=textoPreEntry).grid(column=0,row=3)
    qtd = ttk.Entry(intermediariaFrame)
    qtd.grid(column=0,row=4,padx=100,pady=5)
    ttk.Button(intermediariaFrame,text='Calcular',command=lambda:calcular(int(qtd.get()),rBValue.get(),comb)).grid(column=1,row=4)
    ttk.Label(intermediariaFrame,textvariable=resultado).grid(column=0,row=5)
    ttk.Button(intermediariaFrame,text='Voltar',command=voltar).grid(column=0,row=9,padx=150)
inicio()

root.mainloop()