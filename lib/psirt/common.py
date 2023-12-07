import time
import datetime


class PsirtCommon():
    def __init__(self):
        pass

    def convert_age(self, seconds):
        if seconds > 365 * 60 * 60 * 24:
            years = int(seconds / (365 * 60 * 60 * 24))
            remaining = seconds - years * 365 * 60 * 60 * 24
            days = int(remaining / (60 * 60 * 24))
            return '%sy%sd' % (years, days)

        if seconds > 60 * 60 * 24:
            return '%sd' % (int(seconds / (60 * 60 * 24)))

        if seconds > 60 * 60:
            hours = 0
            while True:
                if seconds < 60 * 60:
                    break

                hours = hours + 1
                seconds = seconds - 60 * 60

            return '%sh%sm' % (
                hours,
                int(seconds / 60)
            )

        if seconds > 60:
            return '%sm' % (int(seconds / 60))

        return '%ss' % (seconds)

    def convert_days(self, seconds):
        if seconds > 60 * 60 * 24:
            return int(seconds / (60 * 60 * 24))

        return 1

    def convert_timestamp(self, timestamp):
        if timestamp is None:
            return None

        new_timestamp = None
        if isinstance(timestamp, str):
            try:
                new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').timetuple()))
            except BaseException:
                pass

            if new_timestamp is None:
                try:
                    new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S%z').timetuple()))
                except BaseException:
                    pass

            if new_timestamp is None:
                try:
                    new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp.rstrip('Z'), '%Y-%m-%dT%H:%M:%S').timetuple()))
                except BaseException:
                    pass

            if new_timestamp is None:
                try:
                    new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f').timetuple()))
                except BaseException:
                    pass

            return new_timestamp

        try:
            new_timestamp = int(timestamp.timestamp())
        except BaseException:
            pass

        return new_timestamp

    def convert_timestamp_to_age(self, timestamp, on_error=None):
        timestamp = self.convert_timestamp(timestamp)
        if timestamp is None:
            return on_error

        return self.convert_age(int(time.time()) - timestamp)

    def convert_timestamp_to_days(self, timestamp, on_error=None):
        timestamp = self.convert_timestamp(timestamp)
        if timestamp is None:
            return on_error

        return self.convert_days(int(time.time()) - timestamp)
