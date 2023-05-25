FROM python:3.8

COPY [".","/usr/src/"]

WORKDIR /usr/src/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app","--host","0.0.0.0","--port","8000"]