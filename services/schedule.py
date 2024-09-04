from datetime import datetime, timedelta
from .parsing import get_schedule

def dict_to_text(data):
    res = ''
    for item in data:
        text = (f"День недели: {item['день_недели']}\n"
                f"Дата: {item['дата'][:10]}\n"
                f"Группа: {item['группа']}\n"
                f"Начало: {item['начало']}\n"
                f"Конец: {item['конец']}\n"
                f"Дисциплина: {item['дисциплина']}\n"
                f"Преподаватель: {item['преподаватель']}\n"
                f"Аудитория: {item['аудитория']}\n")
        res += text
        res += '\n'
    return res

def get_schedule_for_today():
    current_date = datetime.now().date()
    schedule = get_schedule(current_date)
    data = [item for item in schedule if str(current_date) in item['дата']]
    return dict_to_text(data)

def get_schedule_for_tomorrow():
    tomorrow_date = datetime.now().date() + timedelta(days=1)
    schedule = get_schedule(tomorrow_date)
    data = [item for item in schedule if str(tomorrow_date) in item['дата']]
    return dict_to_text(data)

def get_schedule_for_week():
    current_date = datetime.now().date()
    schedule = get_schedule(current_date)
    data = [item for item in schedule]
    return dict_to_text(data)

def get_schedule_for_next_week():
    next_week_date = datetime.now().date() + timedelta(weeks=1)
    schedule = get_schedule(next_week_date)
    data = [item for item in schedule]
    return dict_to_text(data)
