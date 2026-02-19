from lib import filter_helper


class K8sSplunkMonitoringConsoleInfo():
    def __init__(self):
        self.splunk_monitoring_console = None

    def get_splunk_monitoring_console_info(self, splunk_monitoring_console_mo):
        if splunk_monitoring_console_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            splunk_monitoring_console_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(splunk_monitoring_console_mo, 'spec')
        info['status'] = self.get(splunk_monitoring_console_mo, 'status')
        return info

    def get_splunk_monitoring_consoles_info(self, cache_enabled=True):
        if cache_enabled:
            if self.splunk_monitoring_console is not None:
                return self.splunk_monitoring_console

        managed_objects = self.get_splunk_monitoring_console_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.splunk_monitoring_console = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = self.get_splunk_monitoring_console_info(
                managed_object
            )
            info['mo'] = managed_object
            self.splunk_monitoring_console.append(
                info
            )

        return self.splunk_monitoring_console

    def match_splunk_monitoring_console(self, object_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, object_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (object_info['namespace'], object_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_splunk_monitoring_console',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_splunk_monitoring_consoles(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_objects_infos = self.get_splunk_monitoring_consoles_info(cache_enabled=cache_enabled)
        if all_objects_infos is None:
            return None

        object_infos = []

        for object_info in all_objects_infos:
            if not self.match_splunk_monitoring_console(object_info['info'], object_filter):
                continue

            if return_mo:
                object_infos.append(
                    object_info['mo']
                )
                continue

            object_infos.append(
                object_info['info']
            )

        return object_infos

    def is_splunk_monitoring_console(self, namespace, name, cache_enabled=True):
        if self.get_splunk_monitoring_console(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_splunk_monitoring_console(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        objects_info = self.get_splunk_monitoring_consoles(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if objects_info is None:
            return None

        if len(objects_info) == 1:
            return objects_info[0]

        return None
