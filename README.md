# Тестовое задание для 2GIS

## Установка
1. git clone https://github.com/Vebust1/2gis-test-task
2. cd 2gis-test-task
3. pip install -r requirements.txt

# Запуск всех тестов
pytest tests/ -v

# Запуск через Docker

## Собрать образ
docker build -t 2gis-api-tests:01 .

## Запустить тесты
docker run --rm 2gis-api-tests:01
