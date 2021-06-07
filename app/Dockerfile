FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app

COPY  ./ /app

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip


ENV PYTHONUNBUFFERED 1

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]
