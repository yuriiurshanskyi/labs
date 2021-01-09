## Lab_5: Автоматизація за допомогою Makefile VS Docker Compose
### Посилання
+ [Docker Repository](https://hub.docker.com/repository/docker/yuriiurshanskyi/flask)


### Хід роботи

Запускаємо файл app.py
```
pipenv --python 3.8
pipenv install -r requirements.txt
pipenv run python app.py
```
Результат виконання:  
![](./img/localhost_5000.png)  
![](./img/localhost_hits.png)  
![](./img/localhost_logs.png)  

Тестування:
```
pipenv run pytest test_app.py --url http://localhost:5000
```
Тести пройшли успішно

Директиви Makefile:  
+ .PHONY - задаємо псевдоціль  
![](./img/make_PHONY.png)  
+ run - запуск  
![](./img/make_run.png)  
+ test-app - тестування  
![](./img/make_test-app.png)  
+ docker-prune - очищає Docker  
![](./img/make_docker-prune.png)  


Виконуємо `make docker-push`  
![](./img/make_docker-push.png)  
Виконуємо `make docker-wipe`  
![](./img/make_docker-wipe.png)

Перевіряємо версію `docker-compose version`    
![](./img/docker-compose_version.png)  
`docker-compose -p Flask up`  
![](./img/docker-compose_Flask.png)  

Запущений додаток на compose:  
![](./img/localhost.png)  
![](./img/localhost80hits.png)  
![](./img/localhost80logs.png)  

`docker-compose push` - завантажуємо імеджі  
В даному випадку `docker-compose` є кращим за `Makefile`, адже ми працюємо з `Docker`  

`docker-compose -p Django up`  
Демонстрація запуску:  
![](./img/django.png)  
![](./img/django_health.png)  
