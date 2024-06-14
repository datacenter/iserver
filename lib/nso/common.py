import time
import datetime


class NsoCommon():
    def __init__(self):
        pass

    def _get(self, value, key):
        if value is None:
            return '__ERROR'

        if ':' in key:
            subkey = key.split(':')[0]
            if subkey not in value:
                return '__ERROR'

            new_key = ':'.join(key.split(':')[1:])
            return self._get(value[subkey], new_key)

        if key in value:
            return value[key]

        return '__ERROR'

    def get(self, managed_object, key, on_error=None, on_none=None):
        if managed_object is None:
            return on_error

        if not isinstance(managed_object, dict):
            return on_error

        value = self._get(managed_object, key)
        if value == '__ERROR':
            return on_error

        if value is None:
            return on_none

        return value

    def convert_age(self, seconds):
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

    def convert_timestamp(self, timestamp):
        if timestamp is None:
            return None

        new_timestamp = None
        if isinstance(timestamp, str):
            try:
                new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z').timetuple()))
            except BaseException:
                pass

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
