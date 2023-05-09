import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    texto = entrada_texto.get()
    etiqueta.config(text=texto)

ventana = tk.Tk()

frm = ttk.Frame(ventana, padding=10)
frm.grid(column=0, row=0)

etiqueta = ttk.Label(frm, text="Ingresa texto:")
etiqueta.grid(column=0, row=0)

entrada_texto = ttk.Entry(frm)
entrada_texto.grid(column=1, row=0)

boton_mostrar = ttk.Button(frm, text="Mostrar texto", command=mostrar_texto)
boton_mostrar.grid(column=2, row=0)

etiqueta_resultado = ttk.Label(frm, text="")
etiqueta_resultado.grid(column=0, row=1, columnspan=3)

ventana.mainloop()