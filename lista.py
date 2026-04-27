import os

# Esto lee los archivos de la carpeta 'fotos'
archivos = os.listdir('fotos')

# Solo queremos imágenes
fotos = [f for f in archivos if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

print("\n--- COPIÁ DESDE ACÁ ABAJO ---")
for f in fotos:
    print(f"            'fotos/{f}',")
print("--- HASTA ACÁ ---")