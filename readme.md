# Flask-2

## Предварительные шаги

1. Откройте каталог проекта в редакторе VS Code
2. Создайте виртуальное окружение
3. Активируйте виртуальное окружение
4. Установите библиотеку Flask

## Отладка во Flask

1. Создайте файл `app.py` и добавьте в него следующий код:
```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    result = ""
    if 'expression' in request.args:
        print("================================================================================")
        print(request.args)  # Печать отладочного сообщения
        print("================================================================================")
        app.logger.warning(request.args)  # Печать отладочного сообщения
        print("================================================================================")
        result = str(eval(request.args['expression']))
    return render_template("index.html", result=result)
```

Обратите внимание на способы печати отладочных сообщений.

2. Создайте каталог `templates`, создайте в нем файл `index.html` и добавьте в него следующий код:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Учебный сайт</title>
</head>
<body>
    <h1>Добро пожаловать!</h1>
    <form>
        <label>Введите арифметическое выражение (например 2+3):</label>
        <input type="text" name="expression">
        <input type="submit" value="Вычислить">
    </form>
    <p>Результат: {{ result }}</p>
</body>
</html>
```

3. Включите отладочный режим во Flask

Если вы используете PowerShell:
```powershell
$ENV:FLASK_DEBUG=1
```

Если вы используете командную строку:
```cmd
set FLASK_DEBUG=1
```

4. Запустите сервер и обратите внимание на наличие PIN для запуска отладки

```powershell
flask run
```

5. Откройте в браузере адрес [127.0.0.1:5000](http://127.0.0.1:5000) либо [localhost:5000](http://localhost:5000) и убедитесь, что в браузере отображается форма для ввода арифметического выражения.

6. Введите некорректное выражение, вы должны увидеть подобное окно:

![Ошибка](img/error.png)

7. Откройте консоль с запущенным сервером Flask, проверьте что в ней видны отладочные сообщения со значением переменной `request.args`. Сделайте скриншот и сохраните его в каталоге проекта.

8. Вернитесь в браузер, наведите курсор на выделенную строку, нажмите на кнопку с иконкой черного экрана и введите PIN отображаемый в консоли при старте сервера (см. п.4):

9. В открывшемся терминале введите название переменной `request.args` и убедитесь что оно отображает аргументы запроса. Сделайте скриншот и сохраните его в каталоге проекта.

10. Зафиксируйте изменения в новом коммите:

```powershell
git add .
git commit -m "Check Flask debug mode"
```

## Добавление иконки сайта и статических файлов

1. Создайте каталог `static`

2. Найдите сайт с примерами иконок сайтов ([например этот](https://icons8.com/icons/set/favicon-ico), [или этот](https://www.iconfinder.com/search?price=free&license=gte__1)), выберите подходящую, скачайте в формате `ico` и сохраните его в каталог `static` под именем `favicon.ico`.

3. Добавьте тег `link` в тег `head`:

```html
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}">
```

4. Выберите на своем компьютере или в Интернете подходящую картинку и сохраните её в каталоге `static` (в имени файлов не должно быть русских букв, пробелов или специальных символов).

5. Добавьте тег `img` в тело HTML-страницы и замените имя файла:

```html
<img alt="" src="{{ url_for('static', filename='<имя файла>') }}">
```

6. Проверьте отображение иконки сайта и картинки через браузер.

7. Зафиксируйте изменения в новом коммите:

```powershell
git add .
git commit -m "Add favicon and picture to static files"
```

## Дополнительные эндпойнты

1. Добавьте в `app.py` две новые функции:

```
@app.route('/table/')
def table_page():
    return render_template('table.html')


@app.route('/result/<int:x>/<int:y>/')
def result_page(x, y):
    return render_template('result.html', x=x, y=y)
```

2. Добавьте шаблон файла `table.html`:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Учебный сайт</title>
</head>
<body>
    <h1>Таблица умножения</h1>
    <p><a href="{{ url_for('index_page') }}">Главная</a></p>
    <table>
        {% for x in range(1, 11) %}
        <tr>
            {% for y in range(1, 11) %}
            <td>
                <a href="{{ url_for('result_page', x=x, y=y) }}">
                    {{ x }} &times; {{ y }}
                </a>
            </td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

Обратите внимание на синтаксические конструкции в шаблонах.

3. Добавьте шаблон файла `result.html`:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Учебный сайт</title>
</head>
<body>
    <h1>Результат</h1>
    <p><a href="{{ url_for('index_page') }}">Главная</a></p>
    <p><a href="{{ url_for('table_page') }}">Таблица умножения</a></p>
    <p>{{ x * y }}</p>
</body>
</html>
```

4. Добавьте в шаблон `index.html` новую ссылку:

```html
<a href="{{ url_for('table_page') }}">Таблица умножения</a>
```

6. Проверьте работу двух новых страниц на сайте.

7. Зафиксируйте изменения в новом коммите:

```powershell
git add .
git commit -m "Add table of multiplications"
```

## Наследование шаблонов

1. Создайте новый шаблон `base.html`:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}">
    <title>Учебный сайт</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

2. Измените содержимое шаблона `index.html` следующим образом:

```html
{% extends 'base.html' %}

{% block content %}
<h1>Добро пожаловать!</h1>
<form>
    <label>Введите арифметическое выражение (например 2+3):</label>
    <input type="text" name="expression">
    <input type="submit" value="Вычислить">
</form>
<p>Результат: {{ result }}</p>
{% endblock %}
```

3. Убедитесь, что после изменений работа сайта не изменилась

4. Самостоятельно внесите аналогичные изменения в шаблоны `table.html` и `result.html`

5. Зафиксируйте изменения в новом коммите:

```powershell
git add .
git commit -m "Refactor templates"
```
