# Vamos a probar con un archivo que sí tenés
import hashlib
with open("prueba.txt", "rb") as f:
    data = f.read()
    print(f"Archivo: prueba.txt")
    print(f"Tamaño: {len(data)} bytes")
    print(f"MD5: {hashlib.md5(data).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(data).hexdigest()}")

# Si querés analizar un .exe real de tu Windows, copialo a la carpeta ejercicios
# y después descomentá esto:
# analizar_pe("notepad.exe")