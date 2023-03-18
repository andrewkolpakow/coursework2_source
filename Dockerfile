FROM python:3.10-slim

ENV HOME /app
#Чтобы не подставлять везде /app
WORKDIR $HOME

COPY requirements.txt .
#Копируем зависимости requirements.txt в текущую директорию
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .
#Копируем проект целиком в директорию app
CMD flask run -h 0.0.0.0 -p 8080
#Запускаем python для файла с Flask


