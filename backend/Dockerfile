FROM python:3.10-slim

# Instalar dependencias requeridas para Demucs y ffmpeg
RUN apt-get update && apt-get install -y ffmpeg libsndfile1 && apt-get clean

# Crear carpeta de la app
WORKDIR /app

# Copiar requirements
COPY requirements.txt /app/requirements.txt

# Instalar librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos del backend
COPY . /app

# Exponer puerto
EXPOSE 8000

# Comando para iniciar el servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
