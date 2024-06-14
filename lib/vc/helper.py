class VcHelper():
    def __init__(self):
        pass

    def convert_cpu_capacity(self, value, empty_for_zero=False):
        try:
            if value == 0 and empty_for_zero:
                return ''

            unit = ['kHz', 'MHz', 'GHz']
            for index in range(0, 3):
                value = value / 1000
                if value < 1000:
                    break

            if value == 0:
                value = '0 [Hz]'
            else:
                value = '%s [%s]' % (
                    round(value, 2),
                    unit[index]
                )

        except BaseException:
            self.log.error('iwe_cluster_info.convert_cpu_capacity', value)
            return None
        return value

    def convert_cpu_usage(self, value):
        try:
            value = '%s%%' % (int(value))
        except BaseException:
            self.log.error('iwe_cluster_info.convert_cpu_usage', value)
            return None
        return value

    def convert_pct(self, pct, rounded=2):
        try:
            if rounded > 0:
                value = '%s%%' % (round(pct, rounded))
            else:
                value = '%s%%' % (int(pct))

        except BaseException:
            self.log.error('iwe_cluster_info.convert_cpu_capacity', pct)
            return None
        return value

    def convert_memory(self, value, empty_for_zero=False):
        try:
            if value == 0 and empty_for_zero:
                return ''

            unit = ['KiB', 'MiB', 'GiB', 'TiB']
            for index in range(0, 4):
                value = value / 1024
                if value < 1000:
                    break

            if value == 0:
                value = '0 [B]'
            else:
                value = '%s [%s]' % (
                    round(value, 2),
                    unit[index]
                )

        except BaseException:
            self.log.error('iwe_cluster_info.convert_memory', value)
            return None

        return value

    def convert_storage(self, value, empty_for_zero=False):
        try:
            if value == 0 and empty_for_zero:
                return ''

            unit = ['KB', 'MB', 'GB', 'TB']
            for index in range(0, 4):
                value = value / 1024
                if value < 1024:
                    break

            if value == 0:
                value = '0 [B]'
            else:
                value = '%s [%s]' % (
                    round(value, 2),
                    unit[index]
                )

        except BaseException:
            self.log.error('iwe_cluster_info.convert_storage', value)
            return None

        return value

    def convert_speed(self, value, empty_for_zero=False):
        try:
            if value == 0 and empty_for_zero:
                return ''

            unit = ['kbps', 'mbps', 'gbps']
            for index in range(0, 4):
                value = value / 1000
                if value < 1000:
                    break

            if value == 0:
                value = '0'
            else:
                value = '%s [%s]' % (
                    round(value, 0),
                    unit[index]
                )

        except BaseException:
            self.log.error('iwe_cluster_info.convert_speed', value)
            return None

        return value

    def fixup_datastore_folder_name(self, folder):
        if folder == '':
            return '/'

        if not folder.startswith('/'):
            folder = '/%s' % (folder)

        if not folder.endswith('/'):
            folder = '%s/' % (folder)

        return folder

    def fixup_datastore_path(self, path):
        path = path.strip()
        if len(path.split(' ')) == 1:
            return '%s /' % (path)

        items = path.split(' ')
        datastore_name = items[0]
        file_name = ' '.join(items[1:])
        if not file_name.startswith('/'):
            file_name = '/%s' % (file_name)

        return '%s %s' % (datastore_name, file_name)

    def get_parent_folder_name(self, folder_name):
        folder_name = self.fixup_datastore_folder_name(folder_name)

        if folder_name == '/':
            return folder_name

        subfolders = folder_name.lstrip('/').rstrip('/').split('/')[:-1]
        return '/%s/' % ('/'.join(subfolders))

    def get_datastore_file_path(self, folder_name, file_name):
        folder_name = self.fixup_datastore_folder_name(folder_name)
        return '%s%s' % (folder_name, file_name.lstrip('/'))
