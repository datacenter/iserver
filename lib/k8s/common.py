import time
import datetime
import traceback


class K8sCommon():
    def __init__(self):
        pass

    def convert_object(self, item):
        if item is None:
            return None

        if isinstance(item, str):
            return item

        if isinstance(item, int):
            return item

        if isinstance(item, dict):
            converted = {}
            for key in item:
                converted[key] = self.convert_object(
                    item[key]
                )
            return converted

        if isinstance(item, list):
            converted = []
            for key in item:
                converted.append(
                    self.convert_object(
                        key
                    )
                )
            return converted

        converted = str(
            item
        )

        return converted

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
        try:
            if timestamp is None:
                return None

            if isinstance(timestamp, str):
                new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').timetuple()))
            else:
                new_timestamp = int(timestamp.timestamp())

        except BaseException:
            self.log.error(
                'k8s_common.convert_timestamp',
                traceback.format_exc()
            )
            return None

        return new_timestamp
