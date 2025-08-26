from tkinter import Tk, filedialog
import os
import shutil

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

print(len(extensiones))


   
