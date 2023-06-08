# Установка базового образа Python
FROM python:3.10

# Установка рабочей директории
WORKDIR /app

# Копирование файла зависимостей requirements.txt
COPY requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Установка переменной окружения PORT
ENV PORT=3000

# Открываем порт, на котором работает сервер
EXPOSE $PORT

# Запуск приложения
CMD [ "python", "bot.py" ]