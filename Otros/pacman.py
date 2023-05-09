from tkinter import *
from tkinter import ttk, colorchooser
from PIL import ImageTk, Image


class Texto:
    def __init__(self, master):
        self.master = master

        # Crear el campo de entrada y el botón
        self.campo_texto = ttk.Entry(master)
        self.boton_mostrar = ttk.Button(master, text="Mostrar", command=self.mostrar)

        # Crear la etiqueta
        self.etiqueta_texto = ttk.Label(master, text="", foreground="black")

        # Ubicar los widgets en la ventana
        self.campo_texto.grid()
        self.boton_mostrar.grid()
        self.etiqueta_texto.grid()

    def mostrar(self):
        texto = self.campo_texto.get()
        self.etiqueta_texto.config(text=texto)


def elegir_color():
    color = colorchooser.askcolor(title="Selecciona un color")


ventana = Tk()
ventana.title("Prueba")
ventana.geometry("450x700")
frm = ttk.Frame(ventana, padding=10)
frm.grid()
ttk.Label(frm, text="                                                             Hola                                                              ").grid(column=0, row=0)
imagen= Image.open("C:\\Users\\thinktic\\Desktop\\Practicas\\Otros\\gato.gif")
imagen= ImageTk.PhotoImage(imagen)
label_imagen = ttk.Label(ventana, image=imagen)
label_imagen.grid(row=5, column=0)
boton_color = ttk.Button(ventana, text="Elegir color", command=elegir_color)
boton_color.grid(row=10, column=0)
texto2 = Texto(ventana)
ttk.Button(frm, text="Cerrar", command=ventana.destroy).grid(column=0, row=18)
ventana.mainloop()


