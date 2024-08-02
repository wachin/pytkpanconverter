import tkinter as tk
from tkinter import filedialog, ttk
import subprocess

def seleccionar_archivo_entrada():
    extensiones = [".md", ".docx", ".doc", ".odt"]
    tipos_archivo = [("Markdown", "*.md"), ("Word", "*.docx"), ("Word 97-2003", "*.doc"), ("LibreOffice Writer", "*.odt")]
    archivo_entrada.set(filedialog.askopenfilename(filetypes=tipos_archivo))

    # Actualizar las opciones de salida basadas en el archivo de entrada
    ext_entrada = os.path.splitext(archivo_entrada.get())[1].lower()
    if ext_entrada == '.md':
        combo_salida['values'] = ['.odt', '.docx', '.doc']
    else:
        combo_salida['values'] = ['.md']
    combo_salida.set(combo_salida['values'][0])

def seleccionar_archivo_salida():
    ext_salida = combo_salida.get()
    tipos_archivo = [("LibreOffice Writer", "*.odt"), ("Word", "*.docx"), ("Word 97-2003", "*.doc"), ("Markdown", "*.md")]
    archivo_salida.set(filedialog.asksaveasfilename(defaultextension=ext_salida, filetypes=tipos_archivo))

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
ventana.title("Conversor de Documentos")

# Variables para almacenar rutas de archivos
archivo_entrada = tk.StringVar()
archivo_salida = tk.StringVar()
resultado = tk.StringVar()

# Crear y colocar widgets
tk.Button(ventana, text="Seleccionar archivo de entrada", command=seleccionar_archivo_entrada).pack(pady=5)

# Combobox para seleccionar el tipo de archivo de salida
tk.Label(ventana, text="Seleccionar tipo de archivo de salida:").pack(pady=5)
combo_salida = ttk.Combobox(ventana, values=['.odt', '.docx', '.doc', '.md'])
combo_salida.set('.odt')
combo_salida.pack(pady=5)

tk.Button(ventana, text="Seleccionar destino", command=seleccionar_archivo_salida).pack(pady=5)
tk.Button(ventana, text="Ejecutar conversión", command=ejecutar_conversion).pack(pady=5)
tk.Label(ventana, textvariable=resultado).pack(pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
