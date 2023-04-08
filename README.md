## AuthProject
**AuthProject** - приложение, в котором имеется функционал регистрации и авторизации.

### Структура:
Весь функционал прописан в папке `users/`
- `views.py` - вьюшки страниц регистрации, авторизации и главной страницы.
- `forms.py` - формы регистрации и авторизации
- `urls.py` - описана маршрутизация
- `forms.py` - формы для регистрации, авторизации и смены пароля
- `tokens.py` - генератор токена
- `decorators.py` - содержит декоратор `user_not_authenticated`
- `services.py` - содержит функции отправки сообщения на почту пользователя
- в папке `templates/` находятся html файлы
- в `static/users/` находится css файл

### Установка
Проект написан на django framework. В `requirements.txt` указаны нужные пакеты.

### Использование
Главная страница находится по адресу `/users`.
После регистрации (`users/register`) пользователь переходит на страницу авторизации (`users/login`),
а после попадает на главную страницу.

- регистрация с валидацией пароля

<img src="readme_screenshots/reg.png" width="360" height="250">

- авторизация

<img src="readme_screenshots/login.png" width="180" height="120">

В случае когда пользователь забыл пароль, он может нажать на "Забыли пароль?".
После пользователь переходит на страницу `users/password_reset`.

<img src="readme_screenshots/password_reset_request.png" width="420" height="120">

На введенную почту приходит ссылка на смену пароля:

<img src="readme_screenshots/reset_email.png" width="360" height="180">

Перейдя по ссылке, пользователь вводит новый пароль.

<img src="readme_screenshots/password_reset.png" width="320" height="180">

После он переходит на страницу авторизации.