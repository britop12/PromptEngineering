# Introducción a la Ingeniería de Prompts

Este repositorio contiene ejemplos prácticos que complementan la charla sobre  **Ingeniería de Prompts y Agentes Inteligentes con Langchain** . El objetivo de esta charla es proporcionar una comprensión básica de cómo utilizar Langchain para crear aplicaciones avanzadas que combinan la potencia de modelos de lenguaje con agentes inteligentes.

## Contenido del Repositorio

##### Ejemplo de RAG (Retrieval-Augmented Generation)

Este ejemplo demuestra cómo implementar un sistema de generación aumentada con recuperación de información (RAG) utilizando Langchain. Aprenderás cómo combinar la capacidad de generación de un modelo de lenguaje con la recuperación de información relevante desde un conjunto de datos, optimizando así la precisión y relevancia de las respuestas generadas.

##### Ejemplo de Agente de Pandas con Langchain

Este es un ejemplo de un agente inteligente que puede realizar cálculos y análisis de datos utilizando la biblioteca Pandas, demostrando cómo integrar capacidades de manipulación de datos dentro de flujos de trabajo más complejos controlados por agentes.

## Instrucciones para la instalación del proyecto

Estas instrucciones te guiarán paso a paso para obtener una copia del proyecto en funcionamiento en tu máquina local.

##### Prerrequisitos

Python >= 3.10 (Recomendado).

Para verificar la versión de python. Correr el siguiente script en la terminal.

```bash
python --version
```

##### Instalación del proyecto

**1. Clonar el repositorio**

```
git clone https://github.com/britop12/PromptEngineering.git
cd PromptEngineering
```

**2. Configurar el entorno virtual**

```bash
python -m venv prompt
```

**2.1 Activar el entorno virtual:**

* En windows:

```bash
.\prompt\Scripts\activate
```

* En Linux o MacOS:

```
source prompt/bin/activate
```

**3. Instalación de las dependencias**

Una vez activado el entorno virtual, instala las dependencias con el siguiente script:

```bash
pip install -r requirements.txt
```

## Ejecución del código

Dentro del repositorio habrán dos archivos, agent_langchain.py que tendrá la app para hacer consultas con lenguaje natural a archivos de excel o spreadsheet, y rag_app.py que tendrá la app para hacer rag sencillo de acuerdo a una fuente de información en especifico.

Para ejecutar una aplicación ejecutar el siguiente comando:

* Para Agente de pandas con Langchain:

```bash
streamlit run agent_langchain.py
```

* Para la aplicación sencilla de RAG con Langchain:

```bash
streamlit run rag_app.py
```

##### Configuración de las variables de entorno

Para estás aplicaciones se hizo uso de la api de de openAI, por lo tanto es necesario crear la api key desde la plataforma, y en la carpeta del repositorio, usar el archivo ".env_example", cambiar el nombre a ".env" y finalmente pegar ahí la Api Key de openAI.
