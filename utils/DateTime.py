__author__ = 'xiaolei'

import datetime
import time


class DateTime:
    def __init__(self):
        pass

    @staticmethod
    def date_today(pattern='%Y-%m-%d'):
        date_today = ''
        if not pattern or pattern is None:
            date_today = str(datetime.date.today())
        else:
            date_today = time.strftime(pattern)

        return date_today

    @staticmethod
    def starting_time_today():
        date_today = DateTime.date_today()
        time_arr = time.strptime(str(date_today), '%Y-%m-%d')
        return int(time.mktime(time_arr))

    @staticmethod
    def date(pattern='%Y-%m-%d %H:%M:%S', local_time=None):
        if not pattern:
            pattern = '%Y-%m-%d %H:%M:%S'

        # if local_time is None:
        #     local_time = int(time.mktime(datetime.datetime.now().timetuple()))

        if local_time:
            local_time = int(local_time)

        locatime = time.localtime(local_time)
        return time.strftime(pattern, locatime)

    @staticmethod
    def str_to_time(date_time_str, pattern='%Y-%m-%d %H:%M:%S'):
        if not date_time_str:
            return int(time.time())

        if not pattern:
            pattern = '%Y-%m-%d %H:%M:%S'

        time_arr = time.strptime(str(date_time_str), pattern)
        return int(time.mktime(time_arr))

    @staticmethod
    def date_yesterday(pattern='%Y-%m-%d'):
        if not pattern or pattern is None:
            pattern = '%Y-%m-%d'

        return (datetime.datetime.now() + datetime.timedelta(days=-1))\
            .strftime(pattern)




