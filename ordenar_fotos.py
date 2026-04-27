import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

carpeta = "fotos"
fotos = []

for nombre in os.listdir(carpeta):
    if not nombre.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
    
    ruta = os.path.join(carpeta, nombre)
    fecha = None
    
    try:
        img = Image.open(ruta)
        exif = img._getexif()
        if exif:
            for tag_id, valor in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    fecha = datetime.strptime(valor, "%Y:%m:%d %H:%M:%S")
                    break
    except:
        pass
    
    # Si no tiene EXIF, usa la fecha de modificación del archivo
    if not fecha:
        fecha = datetime.fromtimestamp(os.path.getmtime(ruta))
    
    fotos.append((fecha, nombre))

fotos.sort(key=lambda x: x[0])

print("const misFotos = [")
for fecha, nombre in fotos:
    print(f"    'fotos/{nombre}',  // {fecha.strftime('%d/%m/%Y')}")
print("];")