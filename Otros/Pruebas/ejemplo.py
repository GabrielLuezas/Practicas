import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("300x100")

check_var = tk.BooleanVar()
check = tk.Checkbutton(ventana, text="Marca el checkbox", variable=check_var)
check.pack()    

barra = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
barra.pack()

estilo = ttk.Style()
estilo.theme_use('default')

def actualizar_barra():
    if check_var.get():
        estilo.configure("green.Horizontal.TProgressbar", troughcolor='green', bordercolor='green', background='green')
        barra.config(style="green.Horizontal.TProgressbar")         
    else:
        estilo.configure("red.Horizontal.TProgressbar", troughcolor='red', bordercolor='red', background='red')
        barra.config(style="red.Horizontal.TProgressbar")

# Establecer el color de fondo inicial de la barra de progreso
if check_var.get():
    estilo.configure("green.Horizontal.TProgressbar", troughcolor='green', bordercolor='green', background='green')
    barra.config(style="green.Horizontal.TProgressbar")
else:
    estilo.configure("red.Horizontal.TProgressbar", troughcolor='red', bordercolor='red', background='red')
    barra.config(style="red.Horizontal.TProgressbar")

check.config(command=actualizar_barra)

ventana.mainloop()