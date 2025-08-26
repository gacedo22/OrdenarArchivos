import os  # Biblioteca para trabajar con archivos y carpetas
import shutil  # Biblioteca para mover archivos y carpetas

# Ruta donde están los archivos a ordenar
ruta = "C:/Documentos/NuriaSanchezVarios"

# Crear carpetas en destino si no existen
tipos = ["Imágenes", "PDFs", "Vídeos", "Documentos_Word", "Documentos_txt", "Documentos_Excel"]

for carpeta in tipos:
    RutaCarpeta = os.path.join(ruta, carpeta)  # Construye la ruta de las carpetas pero no las crea
    if not os.path.exists(RutaCarpeta):
        os.makedirs(RutaCarpeta)

for archivo in os.listdir(ruta):
    # Evitar mover carpetas creadas
    if os.path.isdir(os.path.join(ruta, archivo)):
        continue

    if archivo.lower().endswith((".jpg", ".png")):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Imágenes", archivo))

    elif archivo.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Vídeos", archivo))

    elif archivo.lower().endswith(".pdf"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "PDFs", archivo))

    elif archivo.lower().endswith((".docx", ".doc")):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_Word", archivo))

    elif archivo.lower().endswith(".txt"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_txt", archivo))

    elif archivo.lower().endswith((".xlsx", ".xls")):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_Excel", archivo))

    else:
        # Si no cumple ninguna extensión, puede quedarse en la carpeta original o mover a una carpeta "Otros"
        # Por ejemplo, para mover a "Otros":
        otros_path = os.path.join(ruta, "Otros")
        if not os.path.exists(otros_path):
            os.makedirs(otros_path)
        shutil.move(os.path.join(ruta, archivo), os.path.join(otros_path, archivo))
