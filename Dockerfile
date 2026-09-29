FROM python:3.11-slim

RUN apt-get update && apt-get install -y binutils yara file && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir jupyterlab pefile yara-python

WORKDIR /lab
COPY ejercicios/ ./ejercicios/

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]