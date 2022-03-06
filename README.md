# Чат-сервер, предоставляющий HTTP API для работы с чатами и сообщениями пользователя.

## Запуск

- Скачайте код
- Настройте окружение. Для этого выполните следующие действия:
  - установите Python3.x;
  - создайте виртуальное окружение [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта и активируйте его.
  - установите необходимые зависимости:

    ```
    pip install -r requirements.txt
    ```
- Создайте файл .env в корне проекта. Сохраните настройки django и базы данных в следующих переменных окружения:
  ```
  DJANGO_SECRET_KEY=django_secret_key
  DATABASE_URL=DATABASE://USER:PASSWORD@HOST:PORT/DATABASENAME
  DJANGO_DEBUG=True или False
  ALLOWED_HOSTS=localhost, HOST
  RUNSERVER_PORT=9000
  ```
- Введите команды для создания базы данных:

```
python manage.py makemigrations
python manage.py migrate
```
- Введите команду для запуска сервера:

```
python manage.py run_server
```

## Основные API методы
Методы обрабатывают HTTP POST запросы c телом, содержащим все необходимые параметры в JSON.

### Добавить нового пользователя
Запрос:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username": "user_1"}' \
  http://localhost:9000/users/add
```
Ответ: id созданного пользователя или HTTP-код ошибки + описание ошибки.

### Создать новый чат между пользователями
Запрос:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name": "chat_1", "users": ["<USER_ID_1>", "<USER_ID_2>"]}' \
  http://localhost:9000/chats/add
```
Ответ: id созданного чата или HTTP-код ошибки + описание ошибки.

Количество пользователей в чате не ограничено.

### Отправить сообщение в чат от лица пользователя
Запрос:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"chat": "<CHAT_ID>", "author": "<USER_ID>", "text": "hi"}' \
  http://localhost:9000/messages/add
```
Ответ: id созданного сообщения или HTTP-код ошибки + описание ошибки.

### Получить список чатов конкретного пользователя
Запрос:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"user": "<USER_ID>"}' \
  http://localhost:9000/chats/get
```

Ответ: cписок всех чатов со всеми полями, отсортированный по времени создания последнего сообщения в чате (от позднего к раннему). Или HTTP-код ошибки + описание ошибки.

### Получить список сообщений в конкретном чате
Запрос:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"chat": "<CHAT_ID>"}' \
  http://localhost:9000/messages/get
```

Ответ: список всех сообщений чата со всеми полями, отсортированный по времени создания сообщения (от раннего к позднему). Или HTTP-код ошибки + описание ошибки.

## Цели проекта
Код написан в учебных целях — это тестовое задание на позицию стажера-бэкендера.