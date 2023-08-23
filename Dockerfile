FROM python:3.11.4

WORKDIR /telegram_bot

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8084

ENTRYPOINT ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8084", "--reload"]