# Ejercicio 1: Detector por firma
# EICAR es un archivo de prueba 100% inofensivo que todos los antivirus detectan.
# Su contenido es este string oficial:

EICAR_STRING = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# TAREA:
# 1. Creá un archivo "prueba.txt" con ese string adentro
# 2. Hacé una función que lea cualquier archivo y detecte si contiene esa firma
# 3. Si lo encuentra, que imprima "ALERTA: Test file detectado"

def escanear_firma(ruta):
    with open(ruta, 'r', errors='ignore') as f:
        contenido = f.read()
        if EICAR_STRING in contenido:
            return True
    return False

# Probalo:
open("prueba.txt", "w").write(EICAR_STRING)
print(escanear_firma("prueba.txt"))