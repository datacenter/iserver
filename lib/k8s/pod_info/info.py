from lib import ip_helper
from lib import filter_helper


class K8sPodInfoInfo():
    def __init__(self):
        self.pod_info = None

    def get_pod_info_info(self, pod_info_mo):
        if pod_info_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            pod_info_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(pod_info_mo, 'spec')
        return info

    def get_pod_infos_info(self, cache_enabled=True):
        if cache_enabled:
            if self.pod_info is not None:
                return self.pod_info

        managed_objects = self.get_pod_info_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.pod_info = []
        for managed_object in managed_objects:
            pod_info_info = {}
            pod_info_info['info'] = self.get_pod_info_info(
                managed_object
            )
            pod_info_info['mo'] = managed_object
            self.pod_info.append(
                pod_info_info
            )

        return self.pod_info

    def match_pod_info(self, pod_info_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, pod_info_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, pod_info_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_pod_info',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_pod_infos(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_pod_infos = self.get_pod_infos_info(cache_enabled=cache_enabled)
        if all_pod_infos is None:
            return None

        pod_infos = []

        for pod_info_info in all_pod_infos:
            if not self.match_pod_info(pod_info_info['info'], object_filter):
                continue

            if return_mo:
                pod_infos.append(
                    pod_info_info['mo']
                )
                continue

            pod_infos.append(
                pod_info_info['info']
            )

        return pod_infos

    def is_pod_info(self, namespace, name, cache_enabled=True):
        if self.get_pod_info(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_pod_info(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        pod_infos = self.get_pod_infos(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pod_infos is None:
            return None

        if len(pod_infos) == 1:
            return pod_infos[0]

        return None
