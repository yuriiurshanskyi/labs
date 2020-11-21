## LAB_3

+ Запускаємо сервер
```
pipenv run python manage.py runserver
```

+ Створюємо темплейт
```
pipenv run python manage.py startapp geralt
```

+ Вносимо зміни до файлів `geralt/settings.py` i `my_site/url.py` (вказуємо __Django__, де шукати сторінки)

+ Заповнюємо файл `geralt/urls.py` з двома посиланнями:
    + на головну сторінку, яку опрацьовує функція __main__
    + на сторінку `/health`, яку опрацьовує функція __health__

+ Встановлюємо бібліотеку, для зндійснення моніторингу за допомогою файлу `monitoring.py` 
```
pipenv install requests
```    

+ Скріни відображених сторінок
[](/images/home.png)
[](/images/health.png)
