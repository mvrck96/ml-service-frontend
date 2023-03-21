# Фронтенд для ML сервсиа

В репозитории находится пример того, как можно написать фронтенд для своего ML сервиса.

Используется только `pyton` код. Это не идеальное решение, оно показывает как можно быстро написать работаюзи UI для бэкэнда.

## Общая информация

Весь код написан на фреймворке `Streamlit`. Связь с бэкендом построена на библиотеке `requests`. Для сборки запроса используются `pydantic` модель. Все можно поднять в докер контейнере и обновлять независимо от бэкенда. Базовая конфигурация через переменные окружения и штатный streamlit конфиг.

## Техстек

- Интерфейс -- `Streamlit`
- Отправка запросов -- `requests`
- Модель данных для запроса -- `pydantic`
- Контейнеризация -- `Dcoker + docker-compose`

## Как пользоваться

Для запуска контейнера с сервисом и всей инфраструктурой:

1. `git clone <repo address>`
2. `cd ml-service-frontend`
3. `cp template.env .env` -- создать копию файла template.env с именем .env
4. Изменить при необходимости переменные окружения
5. При необходимости отредактировать файл `/.streamlit/config.toml`
6. `docker-compose up --build` -- запуск контейнера
7. Адреса:
    UI -- http://localhost:8001

Для локального запуска:
1. `git clone <repo address>`
2. `cd ml-service-frontend`
3. `python3 -m venv venv` -- подготовка виртуального окружения
4. `source venv/bin/activate` -- активация окружения
5. `pip install -r requirements.txt` -- установка зависимостей
6. `cp template.env .env` -- создать копию файла template.env с именем .env
7. Изменить при необходимости переменные окружения
8. При необходимости отредактировать файл `/.streamlit/config.toml`
9. `streamlit run main:app` -- запуск сервиса

> В директории `data` есть файл, который можно использовать в качестве тестового примера !

## Документация

