from tkinter import *
from tkinter import ttk, colorchooser, filedialog
from PIL import ImageGrab
def elegir_color():
    color = colorchooser.askcolor(title="Selecciona un color")[1]
    etiqueta.config(foreground=color)

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        print(f"Se seleccionó el archivo: {ruta_archivo}")

def guardar_texto():
    texto = entrada.get()
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(nombre_archivo, "w") as archivo:
        archivo.write(texto)
def guardar_imagen():
    imagen = ImageGrab.grab()
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".png")
    imagen.save(ruta_archivo)

ventana = Tk()
ttk.Style().theme_use('winnative')
ventana.title("Prueba")
ventana.geometry("250x400")
frm = ttk.Frame(ventana, padding=80)
frm.grid()
color = "black"
etiqueta = ttk.Label(frm, text="Hola", foreground=color)
etiqueta.grid(column=0, row=0)
ttk.Button(frm, text="Cerrar", command=ventana.destroy).grid(column=0, row=3)
boton_color = ttk.Button(ventana, text="Elegir color", command=elegir_color)
boton_color.grid(row=5, column=0)

menu_bar = Menu(ventana)
ventana.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=abrir_archivo)
file_menu.add_command(label="Guardar", command=guardar_imagen)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=ventana.quit)
menu_bar.add_cascade(label="Prueba", menu=file_menu)
entrada = Entry(ventana, width=30)
entrada.grid()
boton_txt = Button(ventana, text="Guardar texto", command=guardar_texto)
boton_txt.grid()

ventana.mainloop()