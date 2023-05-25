## Reto Slack con OpenAI
Este proyecto proporciona una API que integra Slack con OpenAI. La API puede tomar el contenido de un canal de Slack, y utilizando OpenAI, proporciona un resumen condensado de ese canal.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)


## Tecnologías utilizadas
- Python
- FastAPI
- GPT-4 (a través de la API de OpenAI)
- Slack API


## Instalación

1. Clona este repositorio:
```bash
git clone url_repo
```

2. Navega a la carpeta del proyecto:
```bash
cd name_repo
```
3. Crea un entorno virtual e instala las dependencias:
```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
4. Crea un archivo .env en la raíz del proyecto y añade las variables de entorno necesarias, guiate del .env.example

## Ejecución

Para iniciar el servidor de desarrollo de FastAPI, ejecuta el siguiente comando:
```bash
    uvicorn app.main:app --reload
```

## Documentación
La documentación completa de la API, incluidos los puntos finales y los modelos de datos, está disponible en la ruta /docs de la aplicación.

Puedes utilizar herramientas como Postman o Swagger UI para probar los endpoints de la API.


## docker local

antes de ejecutar los comandos docker, crear un .env con las variables de entorno

```bash
docker build -t chat_resume_backend .

docker run -p 8000:8000 -d --add-host host.docker.internal:host-gateway --env-file .env --name chat_resume_backend_v1 chat_resume_backend 

```


