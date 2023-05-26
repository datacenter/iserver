from lib import log_helper


class InfoHelper():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def is_ancestor(self, managed_object, ancestor_type, ancestor_moid):
        if managed_object is None:
            return False

        if 'Ancestors' not in managed_object:
            return False

        for ancestor in managed_object['Ancestors']:
            if ancestor['ObjectType'] == ancestor_type:
                if ancestor['Moid'] == ancestor_moid:
                    return True

        return False

    def get_objects_with_ancestor(self, managed_objects, ancestor_type, ancestor_moid, sort_by=None):
        if managed_objects is None:
            return None

        selected_objects = []
        for managed_object in managed_objects:
            if self.is_ancestor(managed_object, ancestor_type, ancestor_moid):
                selected_objects.append(
                    managed_object
                )

        if sort_by is not None:
            selected_objects = sorted(selected_objects, key=lambda i: i[sort_by])

        return selected_objects

    def convert_cpu_capacity(self, value):
        try:
            value = '%s [GHz]' % (
                int(value / 1000)
            )
        except BaseException:
            self.log.error('info_helper.convert_cpu_capacity', value)
            return None
        return value

    def convert_cpu_usage(self, value):
        try:
            value = '%s%%' % (int(value))
        except BaseException:
            self.log.error('info_helper.convert_cpu_usage', value)
            return None
        return value

    def convert_pct(self, pct):
        try:
            value = '%s%%' % (round(pct, 2))
        except BaseException:
            self.log.error('info_helper.convert_cpu_capacity', pct)
            return None
        return value

    def convert_memory(self, value, precision=2):
        try:
            unit = ['KiB', 'MiB', 'GiB', 'TiB']
            for index in range(0, 4):
                value = value / 1024
                if value < 1000:
                    break

            if precision == 0:
                value = '%s [%s]' % (
                    int(value),
                    unit[index]
                )
            else:
                value = '%s [%s]' % (
                    round(value, precision),
                    unit[index]
                )

        except BaseException:
            self.log.error('info_helper.convert_memory', value)
            return None

        return value

    def convert_storage(self, value):
        try:
            unit = ['KB', 'MB', 'GB', 'TB']
            for index in range(0, 4):
                value = value / 1000
                if value < 1000:
                    break

            value = '%s [%s]' % (
                round(value, 2),
                unit[index]
            )

        except BaseException:
            self.log.error('info_helper.convert_storage', value)
            return None

        return value
