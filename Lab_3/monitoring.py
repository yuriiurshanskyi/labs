import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    while True:
        try:
            r = requests.get(url)
            data = json.loads(r.content)
            logging.info("Сервер доступний. Час на сервері: %s", data['date'])
            logging.info("Запитувана сторінка: : %s", data['current_page'])
            logging.info("Відповідь сервера містить наступні поля:")
            for key in data.keys():
                logging.info("Ключ: %s, Значення: %s", key, data[key])
        except Exception as e:
            logging.error(f'Сталась помилка: {e}')
        return 0
        time.sleep(60)


if __name__ == '__main__':
    main("http://localhost:8000/health")
