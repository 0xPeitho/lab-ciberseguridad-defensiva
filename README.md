# Lab Ciberseguridad Defensiva 🛡️

Laboratorio Docker para análisis de malware 100% defensivo, con fines educativos.

### ¿Qué hace?
Este lab simula el flujo de un analista SOC L1:

**1. Ejercicio 1 - Detección por Firma**
Detecta el archivo de prueba EICAR (estándar de la industria) sin ejecutarlo. Igual que Windows Defender.

**2. Ejercicio 2 - Análisis Estático**
Extrae MD5/SHA256 y busca indicadores sospechosos (IPs, strings) sin ejecutar el binario.

**3. Ejercicio 3 - Auditoría Heurística**
Detecta comportamientos potencialmente maliciosos en código Python: auto-copia `shutil.copy(__file__)` y persistencia en registro `winreg`.

### Cómo probarlo
```bash
docker pull mjr16678/mi-laboratorio-ciberseguridad:latest
docker run -it mjr16678/mi-laboratorio-ciberseguridad