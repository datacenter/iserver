import time
from lib import filter_helper


class K8sLocalVolumeDiscoveryResultInfo():
    def __init__(self):
        self.local_volume_discovery_result = None

    def get_local_volume_discovery_result_info(self, local_volume_discovery_result_mo):
        if local_volume_discovery_result_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            local_volume_discovery_result_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(local_volume_discovery_result_mo, 'spec')
        info['status'] = self.get(local_volume_discovery_result_mo, 'status')

        info['node'] = self.get(local_volume_discovery_result_mo, 'spec:nodeName')
        info['devices'] = []
        info['available_devices'] = []
        info['unavailable_devices'] = []

        devices_mo = self.get(local_volume_discovery_result_mo, 'status:discoveredDevices')
        if devices_mo is not None:
            for device_mo in devices_mo:
                device = {}
                device['__Output'] = {}
                device['wwn'] = None
                device_id = self.get(device_mo, 'deviceID')
                if device_id is not None:
                    try:
                        device['wwn'] = device_id.split('/dev/disk/by-id/')[1]
                    except BaseException:
                        device['wwn'] = device_id

                for key in ['fstype', 'model', 'path', 'property', 'serial', 'size', 'type', 'vendor']:
                    device[key] = self.get(device_mo, key)

                device['sizeT'] = self.info_handler.convert_storage(device['size'])
                device['state'] = self.get(device_mo, 'status:state')
                if device['state'] == 'Available':
                    device['available'] = True
                    device['availableT'] = '\u2713'
                    device['__Output']['availableT'] = 'Green'
                else:
                    device['available'] = False
                    device['availableT'] = '\u2717'
                    device['__Output']['availableT'] = 'Red'

                info['devices'].append(device)
                if device['available']:
                    info['available_devices'].append(
                        device
                    )
                else:
                    info['unavailable_devices'].append(
                        device
                    )

        info['devicesCount'] = len(info['devices'])
        info['availableCount'] = len(info['available_devices'])
        info['unavailableCount'] = len(info['unavailable_devices'])
        info['deviceSummary'] = '%s/%s' % (info['availableCount'], info['devicesCount'])

        return info

    def get_local_volume_discovery_results_info(self, cache_enabled=True):
        if cache_enabled:
            if self.local_volume_discovery_result is not None:
                return self.local_volume_discovery_result

        managed_objects = self.get_local_volume_discovery_result_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.local_volume_discovery_result = []
        for managed_object in managed_objects:
            local_volume_discovery_result_info = {}
            local_volume_discovery_result_info = self.get_local_volume_discovery_result_info(
                managed_object
            )
            local_volume_discovery_result_info['mo'] = managed_object
            self.local_volume_discovery_result.append(
                local_volume_discovery_result_info
            )

        return self.local_volume_discovery_result

    def match_local_volume_discovery_result(self, local_volume_discovery_result_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, local_volume_discovery_result_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, local_volume_discovery_result_info['name']):
                    return False

            if key == 'nodes':
                key_found = True
                found = False
                for item in value.split(','):
                    if filter_helper.match_string(item, local_volume_discovery_result_info['node']):
                        found = True
                        break

                if not found:
                    return False
                
            if not key_found:
                self.log.error(
                    'match_local_volume_discovery_result',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_local_volume_discovery_results(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_local_volume_discovery_results = self.get_local_volume_discovery_results_info(cache_enabled=cache_enabled)
        if all_local_volume_discovery_results is None:
            return None

        local_volume_discovery_results = []

        for local_volume_discovery_result_info in all_local_volume_discovery_results:
            if not self.match_local_volume_discovery_result(local_volume_discovery_result_info, object_filter):
                continue

            if return_mo:
                local_volume_discovery_results.append(
                    local_volume_discovery_result_info['mo']
                )
                continue

            local_volume_discovery_results.append(
                local_volume_discovery_result_info
            )

        return local_volume_discovery_results

    def is_local_volume_discovery_result(self, namespace, name, cache_enabled=True):
        if self.get_local_volume_discovery_result(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_local_volume_discovery_result(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        local_volume_discovery_results = self.get_local_volume_discovery_results(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if local_volume_discovery_results is None:
            return None

        if len(local_volume_discovery_results) == 1:
            return local_volume_discovery_results[0]

        return None

    def wait_local_volume_discovery_result(self, node_name, max_time=360):
        start_time = int(time.time())
        while True:
            results = self.get_local_volume_discovery_results(cache_enabled=False)
            if results is not None:
                for result in results:
                    if result['node'] == node_name:
                        return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_local_volume_discovery_result',
                    'Max time reached: %s' % (node_name)
                )
                return False

            time.sleep(5)
