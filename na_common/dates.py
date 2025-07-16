from datetime import datetime


class EventDate:
    def __init__(self, event_datetime):
        self.event_datetime = datetime.strptime(event_datetime, '%Y-%m-%d %H:%M')


def get_event_date_objs(event_dates):
    event_date_objs = []
    for e in event_dates:
        event_date_objs.append(EventDate(e['event_datetime']))
    return event_date_objs


def get_nice_event_dates(event_dates, show_time=True):
    if event_dates and type(event_dates[0]) is dict:
        event_dates = get_event_date_objs(event_dates)

    event_dates.sort(key=lambda k: k.event_datetime)

    event_date_str = ''
    _event_month = ''
    _event_dates = ''
    for event_date in event_dates:
        m = event_date.event_datetime.strftime("%B")
        d = event_date.event_datetime.strftime("%a %-d, ")
        if 'Tue' in d:
            d = d.replace('Tue', 'Tues')
        elif 'Thu' in d:
            d = d.replace('Thu', 'Thurs')

        if not _event_month:
            _event_month = event_date.event_datetime.strftime("%B")

        if m == _event_month:
            _event_dates += d
        elif _event_dates:
            event_date_str += _event_dates[:-2] + ' of ' + _event_month + ', '
            _event_dates = d
            _event_month = m

    event_date_str = (event_date_str if len(event_date_str) > 2 else '') + _event_dates[:-2] + ' of ' + _event_month

    if show_time:
        event_datetime = event_dates[0].event_datetime
        event_date_str += ' - ' + event_datetime.strftime(
            "%-I:%M %p" if event_datetime.strftime("%M") != '00' else "%-I %p")

    return event_date_str
