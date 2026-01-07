# Usamos una versión ligera de Python (Linux)
FROM python:3.9-slim

# Creamos la carpeta de trabajo dentro de la caja
WORKDIR /app

# Copiamos la lista de ingredientes e instalamos las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo tu código (main.py, modelo.pkl...) dentro
COPY . .

# Avisamos de que usaremos el puerto 8000
EXPOSE 8000

# El comando para arrancar la API cuando enciendas el contenedor
# OJO: Asumo que tu archivo de python se llama 'main.py'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]