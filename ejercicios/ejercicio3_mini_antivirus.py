# Ejercicio 3: Mini-antivirus heurístico
# No crea nada malicioso, solo DETECTA patrones sospechosos en código

PATRONES_SOSPECHOSOS = [
    "shutil.copy(__file__",  # intento de auto-copiarse
    "os.add_dll_directory",
    "winreg.CreateKey", # modificar registro para persistencia
]

def auditoria_codigo(ruta_codigo):
    with open(ruta_codigo, 'r') as f:
        code = f.read()
        score = 0
        for patron in PATRONES_SOSPECHOSOS:
            if patron in code:
                print(f"[SOSPECHOSO] Patrón encontrado: {patron}")
                score += 1
        if score >= 2:
            print("-> Clasificación: COMPORTAMIENTO POTENCIALMENTE MALICIOSO")
        else:
            print("-> Clasificación: Limpio")

# TAREA: Crea un archivo "codigo_a_auditar.py" con alguno de esos patrones
# y pasalo por esta función.