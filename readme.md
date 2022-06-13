#Тестовое задание Кожинов В.С.
##Подготовка проекта
Создание миграций и загрузка fixtures.json
В Фикстурах находятся:
- админ с данными `admin admin`;
- Наполнение базы assignment.models.Color цветами blue, green, red;


    docker-compose prepareproject

## Запуск проекта

    docker-compose up web

### Необходимые урлы
- /equation/solve/ - решение квадратных уравнений;
- /assignment/get-item/ - выборка предметов;

## Запуск тестов 

    docker-compose up test