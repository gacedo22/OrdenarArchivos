#Versión con ventana emergente para introducir carpeta

from tkinter import Tk, filedialog
import os
import shutil

# Ruta donde están los archivos a ordenar
#ruta = "C:/Documentos/Cosas de niños"

ventana=Tk()
ventana.withdraw()
ruta=filedialog.askdirectory(title="Seleccionar Carpeta a Ordenar")


# Diccionario de extensiones asociadas a carpetas
extensiones = {
    # Imágenes
    ".jpg": "Imágenes", ".jpeg": "Imágenes", ".png": "Imágenes",
    ".gif": "Imágenes", ".bmp": "Imágenes", ".tiff": "Imágenes",
    ".svg": "Imágenes", ".webp": "Imágenes",

    # Documentos
    ".pdf": "PDFs", ".doc": "Documentos_Word", ".docx": "Documentos_Word",
    ".txt": "Documentos_txt", ".rtf": "Documentos_txt", ".odt": "Documentos_Word",
    ".xlsx": "Documentos_Excel", ".xls": "Documentos_Excel", ".csv": "Documentos_Excel",
    ".ppt": "Presentaciones", ".pptx": "Presentaciones",

    # Vídeos
    ".mp4": "Vídeos", ".avi": "Vídeos", ".mov": "Vídeos", ".mkv": "Vídeos", ".wmv": "Vídeos",

    # Audio
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio", ".m4a": "Audio",

    # Comprimidos
    ".zip": "Comprimidos", ".rar": "Comprimidos", ".7z": "Comprimidos",
    ".tar": "Comprimidos", ".gz": "Comprimidos",

    # Código
    ".py": "Código_Python", ".js": "Código_JavaScript", ".ts": "Código_JavaScript",
    ".html": "Código_Web", ".css": "Código_Web", ".php": "Código_Web",
    ".java": "Código_Java", ".c": "Código_C", ".cpp": "Código_Cpp", ".cs": "Código_CSharp",
    ".json": "Datos", ".xml": "Datos", ".sql": "Bases_de_datos", ".ipynb": "Jupyter_Notebooks",
    ".sh": "Scripts", ".bat": "Scripts", ".ps1": "Scripts",

    # Ejecutables
    ".exe": "Instaladores", ".msi": "Instaladores", ".iso": "Imágenes_Disco",
}

# Diccionario para agrupar archivos por carpeta de destino
archivos_por_carpeta = {}

# 1. Recorremos los archivos para saber qué carpetas hacen falta
for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    if os.path.isfile(ruta_archivo):
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower()
        if ext in extensiones:
            carpeta = extensiones[ext]
            if carpeta not in archivos_por_carpeta:
                archivos_por_carpeta[carpeta] = []
            archivos_por_carpeta[carpeta].append(archivo)

# 2. Creamos solo las carpetas necesarias
for carpeta in archivos_por_carpeta:
    ruta_carpeta = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# 3. Movemos los archivos a sus carpetas correspondientes
for carpeta, archivos in archivos_por_carpeta.items():
    for archivo in archivos:
        origen = os.path.join(ruta, archivo)
        destino = os.path.join(ruta, carpeta, archivo)
        shutil.move(origen, destino)

print("Archivos organizados correctamente.")
