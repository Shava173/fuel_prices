# Використання базового образу з Python 3.12
FROM python:3.12-slim

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлів до контейнера
COPY requirements.txt requirements.txt
COPY app/ app/

# Встановлення залежностей
RUN pip install -r requirements.txt

# Встановлення змінної середовищ
