import requests

def get_schedule(current_date):
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
                "дисциплина": item["дисциплина"],
                "преподаватель": item["преподаватель"],
                "аудитория": item["аудитория"]
            }
            result.append(entry)
        return result
    else:
        return r

