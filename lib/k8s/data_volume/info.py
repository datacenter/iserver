import time

from lib import filter_helper


class K8sDataVolumeInfo():
    def __init__(self):
        self.data_volume = None

    def get_data_volume_info(self, data_volume_mo):
        if data_volume_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            data_volume_mo
        )
        info.update(metadata_info)

        info['access_modes'] = self.get(data_volume_mo, 'spec:pvc:accessModes', on_error=[], on_none=[])
        info['storage'] = self.get(data_volume_mo, 'spec:pvc:resources:requests:storage')

        info['claim_name'] = self.get(data_volume_mo, 'status:claimName')
        info['phase'] = self.get(data_volume_mo, 'status:phase')
        info['progress'] = self.get(data_volume_mo, 'status:progress')

        conditions = self.get(data_volume_mo, 'status:conditions', on_error=[], on_none=[])

        info['bound'] = False
        info['ready'] = False
        info['running'] = False

        for condition in conditions:
            if condition['type'] == 'Bound':
                if condition['status'] == 'True':
                    info['bound'] = True

            if condition['type'] == 'Ready':
                if condition['status'] == 'True':
                    info['ready'] = True

            if condition['type'] == 'Running':
                if condition['status'] == 'True':
                    info['running'] = True

        if info['ready']:
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['readyTick'] = '\u2717'
            info['__Output']['readyTick'] = 'Red'

        if info['running']:
            info['runningTick'] = '\u2713'
            info['__Output']['runningTick'] = 'Green'
        else:
            info['runningTick'] = '\u2717'
            info['__Output']['runningTick'] = 'Red'

        if info['bound']:
            info['boundTick'] = '\u2713'
            info['__Output']['boundTick'] = 'Green'
        else:
            info['boundTick'] = '\u2717'
            info['__Output']['boundTick'] = 'Red'

        return info

    def get_data_volumes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.data_volume is not None:
                return self.data_volume

        managed_objects = self.get_data_volume_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.data_volume = []
        for managed_object in managed_objects:
            data_volume_info = {}
            data_volume_info['info'] = self.get_data_volume_info(
                managed_object
            )
            data_volume_info['mo'] = managed_object
            self.data_volume.append(
                data_volume_info
            )

        return self.data_volume

    def match_data_volume(self, data_volume_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, data_volume_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (data_volume_info['namespace'], data_volume_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_data_volume',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_data_volumes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_data_volumes = self.get_data_volumes_info(cache_enabled=cache_enabled)
        if all_data_volumes is None:
            return None

        data_volumes = []

        for data_volume_info in all_data_volumes:
            if not self.match_data_volume(data_volume_info['info'], object_filter):
                continue

            if return_mo:
                data_volumes.append(
                    data_volume_info['mo']
                )
                continue

            data_volumes.append(
                data_volume_info['info']
            )

        return data_volumes

    def is_data_volume(self, namespace, name, cache_enabled=True):
        if self.get_data_volume(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_data_volume(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        data_volumes = self.get_data_volumes(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if data_volumes is None:
            return None

        if len(data_volumes) == 1:
            return data_volumes[0]

        return None

    def wait_data_volume_upload_ready(self, namespace, name, max_time=60, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            pvc_info = self.get_data_volume(
                namespace,
                name,
                cache_enabled=False
            )
            if pvc_info is not None:
                if pvc_info['phase'] == 'UploadReady':
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_data_volume_upload_ready',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)
