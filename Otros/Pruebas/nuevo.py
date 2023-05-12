import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("350x100")

style = ttk.Style()
style.theme_use('default')
style.configure("blue.Horizontal.TProgressbar", background='pink', troughcolor='white')

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", style="blue.Horizontal.TProgressbar")
progress.pack(pady=10)

def update_progress():
    progress["value"] += 10
    if progress["value"] < 100:
        root.after(1000, update_progress)
    else:
        messagebox.showinfo("Mensaje de alerta", "¡Proceso completado con éxito!")

def reset_progress():
    progress["value"] = 0

start_button = tk.Button(root, text="Comenzar", command=update_progress)
start_button.pack(side="left", padx=10)

reset_button = tk.Button(root, text="Reiniciar", command=reset_progress)
reset_button.pack(side="left", padx=10)

root.mainloop()