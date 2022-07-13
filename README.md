# Testing

## Для запуска проекта:

* Для запуска проекта склонируйте его. Командой git clone.

* Затем создайте виртуальное окружение venv. Командой python3.8 -m venv venv.

* После запустите окружение. Вот так source venv/bin/activate

* Теперь надо установить зависимости, которые находятся в файле requirements.txt. Командой pip install -r requirements.txt

* Применим миграции python3.8 manage.py migrate

* Надо поставить фикстуры командой python3.8 manage.py loaddata fixtures/dump.json.

* И теперь просто запускаем проект python3.8 manage.py runserver

## Использовал:
* Python3.8
* Postgresql
* Django
* DRF
