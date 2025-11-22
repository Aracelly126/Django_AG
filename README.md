# 🌡️ Conversor Celsius a Fahrenheit con TensorFlow y Django

Este proyecto implementa un **modelo de Machine Learning** que convierte temperaturas de **Celsius a Fahrenheit** utilizando una red neuronal, con un **frontend web interactivo** desarrollado en **Django**.

---

## 🚀 Características

- **Modelo de ML**: Red neuronal entrenada para conversión de temperatura.  
- **Backend API**: Endpoint RESTful con Django.  
- **Frontend Interactivo**: Interfaz web responsive y amigable.  
- **Fácil Integración**: API sencilla para desarrolladores.

---

## 🛠️ Tecnologías Utilizadas

- Python 3.8+  
- Django 4.x  
- TensorFlow/Keras  
- NumPy  
- HTML / CSS / JavaScript

---

## 📦 Instalación

### Prerrequisitos

```bash
python --version   # Debe ser 3.8 o superior
pip --version      # Gestor de paquetes de Python
````

##1️⃣ Clonar y configurar entorno
### Clonar el repositorio
git clone <tu-repositorio>
cd <directorio-del-proyecto>

### Crear entorno virtual (opcional pero recomendado)
python -m venv venv

### Activar entorno virtual
source venv/bin/activate    # Linux/Mac
### venv\Scripts\activate     # Windows

### Instalar dependencias
pip install django tensorflow numpy


## 🎯 Frontend

- La aplicación incluye una interfaz web donde puedes:

- Ingresar temperaturas en Celsius.

- Ver la conversión instantánea a Fahrenheit.

- Interactuar con el modelo de Machine Learning.

## 🤖 Sobre el Modelo

- Arquitectura: Red neuronal simple.

- Entrenamiento: Modelo preentrenado para conversión precisa.

- Precisión: Alta exactitud en el rango de temperaturas comunes.

## 🐛 Solución de Problemas

- Error: "Modelo no cargado"

- Verifica que modelo_c2f.keras esté en la ruta correcta.

- Confirma que TensorFlow esté instalado correctamente.

- Error: JSON inválido

- Asegúrate de enviar contenido como JSON válido.

- Verifica que el header Content-Type: application/json esté presente.

### Dependencias faltantes

pip install --upgrade tensorflow django numpy

## 📊 Ejemplos de Conversión
Celsius	Fahrenheit
0°C	32°F
20°C	68°F
37°C	98.6°F
100°C	212°F
👨‍💻 Desarrollo

## Para contribuir al proyecto:

- Forkea el repositorio.

- Crea una rama para tu feature (git checkout -b feature/nueva-funcion).

- Realiza tus cambios y commitea (git commit -m "Agrega nueva función").

- Abre un Pull Request.

### ✨ ¡Gracias por usar y contribuir a este proyecto!
