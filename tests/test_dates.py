from datetime import datetime

from na_common.dates import get_nice_event_dates


class MockEventDates:
    def __init__(self, event_datetime):
        self.event_datetime = datetime.strptime(event_datetime, "%Y-%m-%d %H:%M")


def test_get_nice_event_dates():
    event_dates = [
        MockEventDates('2019-01-01 12:00'),
        MockEventDates('2019-01-15 12:00'),
        MockEventDates('2019-02-05 12:00')
    ]
    nice_event_dates = get_nice_event_dates(event_dates)
    assert nice_event_dates == 'Tue 1, Tue 15 of January, Tue 5 of February - 12 PM'


def test_get_nice_event_dates_with_dict():
    event_dates = [
        {
            "event_datetime": "2019-01-01 12:00",
        },
        {
            "event_datetime": "2019-01-08 12:00",
        },
        {
            "event_datetime": "2019-02-05 12:00",
        }
    ]
    nice_event_dates = get_nice_event_dates(event_dates)
    assert nice_event_dates == 'Tue 1, Tue 8 of January, Tue 5 of February - 12 PM'
