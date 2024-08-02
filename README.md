# pytkpanconverter
Interfaz gráfica en TKinter para convertir archivos markdown a LibreOffice con pandoc

En Debian, `tkinter` no viene preinstalado por defecto con Python, para instalar `tkinter` en Debian 12, necesitas instalar el paquete `python3-tk`. Aquí están los pasos que debes seguir junto a las demás dependencias:

1. Abre una terminal.

2. Actualiza la lista de paquetes de tu sistema: 

```
sudo apt update
```

Instala los paquetes:

```
sudo apt install pandoc python3-tk tk-dev
```

Después de instalar estos paquetes, deberías poder ejecutar el script sin problemas.

Para lanzar el programa ponga en una terminal en el lugar donde está el programa:

```
python3 pytkconverter2.py
```

Este código  incluye las siguientes caracteristicas:

1. Permite seleccionar archivos de entrada en formatos .md, .docx, .doc y .odt.
2. Añade un menú desplegable (Combobox) para seleccionar el tipo de archivo de salida.
3. Las opciones de salida se actualizan dinámicamente según el tipo de archivo de entrada: 
   - Si el archivo de entrada es .md, las opciones de salida son .odt, .docx y .doc.
   - Si el archivo de entrada es .docx, .doc o .odt, la única opción de salida es .md.
4. El diálogo para guardar el archivo ahora usa la extensión seleccionada en el Combobox.

Algunas conversiones pueden requerir filtros o opciones adicionales de pandoc para obtener los mejores resultados los cuales aún no hace este programa