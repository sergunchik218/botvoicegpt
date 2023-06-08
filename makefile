# Переменные
IMAGE_NAME=botvoice
CONTAINER_NAME=botvoice_container

# Сборка Docker-образа
build:
	docker build -t botvoice .

# Запуск Docker-контейнера
run:
    docker run -d --name botvoice_container botvoice


# Остановка Docker-контейнера
stop:
    docker stop botvoice_container
    docker rm botvoice_container

# Очистка
clean:
    docker rmi botvoice

# По умолчанию выполняется сборка и запуск контейнера
default: build run
