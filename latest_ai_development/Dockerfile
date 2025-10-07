# Usa una imagen oficial de Python como imagen base
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala los paquetes necesarios
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Crea el directorio de datos y asigna los permisos correctos
RUN mkdir -p /app/data && chown -R 1000:1000 /app/data

# Expone el puerto 7860 para Gradio
EXPOSE 7860

# Expone el puerto 8000 para FastAPI
EXPOSE 8000

# Define las variables de entorno
ENV OPENAI_API_KEY=""
ENV PERPLEXITY_API_KEY=""
ENV XDG_DATA_HOME="/app/data"

# Ejecuta app.py cuando el contenedor se inicie
CMD ["python", "app.py"]
