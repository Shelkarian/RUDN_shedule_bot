from datetime import datetime, timedelta
from parsing import get_schedule

def get_schedule_for_today():
    current_date = datetime.now().date()
    schedule = get_schedule(current_date)
    return [item for item in schedule if str(current_date) in item['дата']]

def get_schedule_for_tomorrow():
    tomorrow_date = datetime.now().date() + timedelta(days=1)
    schedule = get_schedule(tomorrow_date)
    return [item for item in schedule if str(tomorrow_date) in item['дата']]

def get_schedule_for_week():
    current_date = datetime.now().date()
    schedule = get_schedule(current_date)
    return [item for item in schedule]

def get_schedule_for_next_week():
    next_week_date = datetime.now().date() + timedelta(days=7)
    schedule = get_schedule(next_week_date)
    return [item for item in schedule if str(next_week_date) in item['дата']]
