import datetime as dt


def date_in_future(days_count=0):
    current_time = dt.datetime.now()
    if type(days_count) is int:
        period_time = dt.timedelta(days=days_count)
        current_time += period_time

    return current_time.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future())
