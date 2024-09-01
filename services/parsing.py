import requests
import datetime


def get_shedule(current_date):
    if current_date == 0:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    result = []
    r = requests.get('https://mmis-web.rudn-sochi.ru/api/Rasp?idGroup=2177&sdate={current_date}}')
    if r.status_code == 200:
        for item in r.json()['data']['rasp']:
            entry = {
                "день_недели": item["день_недели"],
                "дата": item["дата"],
                "группа": item["группа"],
                "начало": item["начало"],
                "конец": item["конец"],
                "часы": item["часы"],
                "дисциплина": item["дисциплина"],
                "преподаватель": item["преподаватель"],
                "аудитория": item["аудитория"]
            }
            result.append(entry)
        return result
    else:
        return r

