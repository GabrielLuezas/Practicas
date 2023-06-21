# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del directorio actual a la imagen
COPY apinueva.py /app

COPY . /app

# Instalar las dependencias de la API
RUN pip install -r requirements.txt

# Exponer el puerto en el que se ejecutará la API
EXPOSE 4000

# Comando para iniciar la API cuando se ejecute el contenedor
CMD ["python", "apinueva.py"]