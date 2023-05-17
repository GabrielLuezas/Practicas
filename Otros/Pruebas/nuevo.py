import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("350x100")

style = ttk.Style()
style.theme_use('default')
style.configure("blue.Horizontal.TProgressbar", background='pink', troughcolor='white')

progress = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate", style="blue.Horizontal.TProgressbar")
progress.pack(pady=10)

def update_progress():
    progress["value"] += 25
    if progress["value"] < 100:
        ventana.after(1000, update_progress)
    else:
        messagebox.showinfo("Mensaje de alerta", "¡Proceso completado con éxito!")

def reset_progress():
    progress["value"] = 0

start_button = tk.Button(ventana, text="Comenzar", command=update_progress)
start_button.pack(side="left", padx=10)

reset_button = tk.Button(ventana, text="Reiniciar", command=reset_progress)
reset_button.pack(side="left", padx=10)
ventana.mainloop()