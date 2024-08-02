import tkinter as tk
from tkinter import filedialog
import subprocess

def seleccionar_archivo_entrada():
    archivo_entrada.set(filedialog.askopenfilename(filetypes=[("Markdown", "*.md")]))

def seleccionar_archivo_salida():
    archivo_salida.set(filedialog.asksaveasfilename(defaultextension=".odt", filetypes=[("LibreOffice Writer", "*.odt")]))

def ejecutar_conversion():
    entrada = archivo_entrada.get()
    salida = archivo_salida.get()
    if entrada and salida:
        try:
            subprocess.run(["pandoc", entrada, "-o", salida], check=True)
            resultado.set("Conversión completada con éxito.")
        except subprocess.CalledProcessError:
            resultado.set("Error en la conversión.")
    else:
        resultado.set("Por favor, seleccione archivos de entrada y salida.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor Markdown a ODT")

# Variables para almacenar rutas de archivos
archivo_entrada = tk.StringVar()
archivo_salida = tk.StringVar()
resultado = tk.StringVar()

# Crear y colocar widgets
tk.Button(ventana, text="Seleccionar archivo Markdown", command=seleccionar_archivo_entrada).pack(pady=5)
tk.Button(ventana, text="Seleccionar destino ODT", command=seleccionar_archivo_salida).pack(pady=5)
tk.Button(ventana, text="Ejecutar conversión", command=ejecutar_conversion).pack(pady=5)
tk.Label(ventana, textvariable=resultado).pack(pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
