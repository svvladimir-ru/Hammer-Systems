# Hammer-Systems

### Требования


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
$ celery -A hammer worker --loglevel=INFO
```

Свернуть окно, оставив воркер работать самостоятельно.

### После всех действий можно полностью работать с сервисом.

## Авторы

* **Vladimir Svetlakov** - [svvladimir-ru](https://github.com/svvladimir-ru)