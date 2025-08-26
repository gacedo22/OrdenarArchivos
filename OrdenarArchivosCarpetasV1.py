import os  # Biblioteca para trabajar con archivos y carpetas
import shutil  # Biblioteca para mover archivos y carpetas

# Ruta donde están los archivos a ordenar
ruta = "C:/Documentos/Cosas de niños"

# Crear carpetas en destino si no existen
#tipos = ["Imágenes", "PDFs", "Vídeos", "Documentos_Word", "Documentos_txt", "Documentos_Excel"]

extensiones = {
    # Imágenes
    ".jpg": "Imágenes",
    ".jpeg": "Imágenes",
    ".png": "Imágenes",
    ".gif": "Imágenes",
    ".bmp": "Imágenes",
    ".tiff": "Imágenes",
    ".svg": "Imágenes",
    ".webp": "Imágenes",

    # Documentos
    ".pdf": "PDFs",
    ".doc": "Documentos_Word",
    ".docx": "Documentos_Word",
    ".txt": "Documentos_txt",
    ".rtf": "Documentos_txt",
    ".odt": "Documentos_Word",
    ".xlsx": "Documentos_Excel",
    ".xls": "Documentos_Excel",
    ".csv": "Documentos_Excel",
    ".ppt": "Presentaciones",
    ".pptx": "Presentaciones",

    # Vídeos
    ".mp4": "Vídeos",
    ".avi": "Vídeos",
    ".mov": "Vídeos",
    ".mkv": "Vídeos",
    ".wmv": "Vídeos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".m4a": "Audio",

    # Archivos comprimidos
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
    ".7z": "Comprimidos",
    ".tar": "Comprimidos",
    ".gz": "Comprimidos",

    # Archivos de código (programador)
    ".py": "Código_Python",
    ".js": "Código_JavaScript",
    ".ts": "Código_JavaScript",
    ".html": "Código_Web",
    ".css": "Código_Web",
    ".php": "Código_Web",
    ".java": "Código_Java",
    ".c": "Código_C",
    ".cpp": "Código_Cpp",
    ".cs": "Código_CSharp",
    ".json": "Datos",
    ".xml": "Datos",
    ".sql": "Bases_de_datos",
    ".ipynb": "Jupyter_Notebooks",
    ".sh": "Scripts",
    ".bat": "Scripts",
    ".ps1": "Scripts",

    # Instaladores y ejecutables
    ".exe": "Instaladores",
    ".msi": "Instaladores",
    ".iso": "Imágenes_Disco",
}


for carpeta in set(extensiones.values()):
    RutaCarpeta = os.path.join(ruta, carpeta)  # Construye la ruta de las carpetas pero no las crea
    if not os.path.exists(RutaCarpeta):
        os.makedirs(RutaCarpeta)

for archivo in os.listdir(ruta): #lee los archivos y las carpetas que hay en ruta
    RutaArchivos=os.path.join(ruta,archivo)
    if os.path.isfile(RutaArchivos):
        nombre,ext=os.path.splitext(archivo)
        ext=ext.lower()
        
        if ext in extensiones:
            destino=os.path.join(ruta,extensiones[ext],archivo)
            shutil.move(RutaArchivos,destino)
