# Hammer-Systems

### Требования

Создать файл в проекте .env со следующими полями:

* DB_ENGINE=django.db.backends.postgresql_psycopg2 # указываем, что работаем с postgresql
* DB_NAME=# имя базы данных
* DB_USER=# логин для подключения к базе данных
* DB_PASSWORD=# пароль для подключения к БД (установите свой)
* DB_HOST=127.0.0.1 # название сервиса (контейнера)
* DB_PORT=5432 # порт для подключения к БД
* EMAIL_HOST=smtp.gmail.com  # smtp host пример gmail
* EMAIL_PORT=587  # порт 
* EMAIL_HOST_USER= # почта ...@gmail.com
* EMAIL_HOST_PASSWORD= # пароль

[Python](https://www.python.org/downloads/) v3.7 +  для запуска.
Установите зависимости и виртуальное окружение и запустите сервер.

```sh
$ pip install virtualenv
$ virtualenv 'название виртуального окружения', либо python3 -m venv 'название виртуального окружения'
$ venv 'название виртуального окружения'/Scripts(или bin для linux)/activate
$ pip install -r requirements.txt
$ python manage.py collectstatic
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Так же понадобится docker для удобного запуска redis

[Docker](https://www.docker.com/)

Установка для linux
```sh
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
$ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$ (lsb_release -cs) \
$ stable"
$ sudo apt update
$ sudo apt install docker-ce -y
```

После установки выполнить следующие команды:

```sh
$ docker run -d -p 6379:6379 redis
```

И находясь в папке проекта
```sh
$ celery -A hammer worker --loglevel=INFO
```

Свернуть окно, оставив воркер работать самостоятельно.

### После всех действий можно полностью работать с сервисом.

## Авторы

* **Vladimir Svetlakov** - [svvladimir-ru](https://github.com/svvladimir-ru)
