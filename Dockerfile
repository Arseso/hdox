FROM python:3.10
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY src /app/src
COPY ./requirements.txt .
EXPOSE 8000
ENTRYPOINT ["uvicorn", "src.web.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]