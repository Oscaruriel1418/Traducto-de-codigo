
#  CodeMorph Auto: Asistente de Código con IA

> Una herramienta potente para **traducir** y **explicar** código utilizando la inteligencia artificial de Google Gemini.

## Descripción

**CodeMorph Auto** es una aplicación web construida con Python y Streamlit que actúa como tu compañero de programación. Utiliza la API de Google Generative AI para entender código complejo y convertirlo a otros lenguajes o explicártelo paso a paso en español.

A diferencia de otros scripts, esta versión incluye **Detección Automática de Modelos**, lo que evita errores de compatibilidad (como el error 404) ajustándose automáticamente a la versión de Gemini que tu cuenta tenga habilitada 

##  Características Principales

* ** Traductor Políglota:** Convierte código entre Python, JavaScript, Java, C++, Go, Rust y más.
* ** Modo Profesor:** Explica la lógica de cualquier fragmento de código paso a paso en español.
* ** Auto-Configuración:** Detecta automáticamente qué modelo de IA tienes disponible para evitar fallos.
* ** Interfaz Rápida:** UI limpia y moderna gracias a Streamlit.

##  Requisitos Previos

Antes de empezar, asegúrate de tener instalado:

1.  **Python** (versión 3.8 o superior).
2.  Una **API Key de Google** (puedes obtenerla gratis en [Google AI Studio](https://aistudio.google.com/)).

##  Instalación

1.  **Clona este repositorio** (o descarga los archivos):
    ```bash
    git clone <tu-repositorio-url>
    cd tu-carpeta
    ```

2.  **Instala las dependencias necesarias:**
    Abre tu terminal y ejecuta:
    ```bash
    pip install streamlit google-generativeai
    ```

##  Configuración

1.  Abre el archivo `app.py` en tu editor de código.
2.  Busca la línea 7 donde dice `MI_API_KEY`.
3.  Pega tu clave API dentro de las comillas:

    ```python
    # app.py
    MI_API_KEY = "AIzaSyD2..." # <- Tu clave real aquí
    ```

    > **Nota:** El código incluye una función `.strip()` para limpiar espacios en blanco accidentales al copiar y pegar.

##  Cómo Ejecutar

Una vez configurada la clave, ejecuta el siguiente comando en tu terminal:

```bash
streamlit run app.py
