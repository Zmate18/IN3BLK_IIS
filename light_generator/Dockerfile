FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY generator.py .

CMD ["sh", "-c", "sleep 10 && python -u generator.py"]