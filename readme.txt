Используемые технологии:
- Язык программирования: Python 3.12.1
- Фреймворк: Django 5.1.5
- База данных: SQLite
- Фронтенд: HTML, CSS, Bootstrap, JS
- Виртуальное окружение: venv

Инструкция по установке проекта к себе на пк:

1️⃣ Распаковать архив
Сначала распакуй logistic.zip в удобную папку. Например, в D:\new_folder\logistic

2️⃣ Открыть терминал в папке проекта
Открой Командную строку (CMD) или PowerShell, затем перейди в папку проекта:
cd D:\new_folder\logistic

3️⃣ Создать и активировать виртуальное окружение
Создай виртуальное окружение (чтобы изолировать зависимости проекта):

python -m venv venv или python3 -m venv venv (попробуй оба варианта)

Активируй его:
Если используешь CMD:
venv\Scripts\activate

Если используешь PowerShell:
venv\Scripts\Activate.ps1
⚠️ Если появится ошибка "execution policy error", введи:
Set-ExecutionPolicy Unrestricted -Scope Process

4️⃣ Установить зависимости
Если у проекта есть файл requirements.txt, установи все нужные зависимости:
pip install -r requirements.txt

5️⃣ Применить миграции базы данных

Команда для настройки БД:
python manage.py migrate

6️⃣ Создать суперпользователя (если нужно админ-панель)
python manage.py createsuperuser
Введи имя пользователя, email(необязательно) и пароль.

7️⃣ Запустить сервер
Запусти локальный сервер Django:
python manage.py runserver

После этого открой браузер и перейди по адресу:
http://127.0.0.1:8000/
или
http://localhost:8000/
