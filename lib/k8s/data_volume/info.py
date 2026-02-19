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

        info['claim_name'] = self.get(data_volume_mo, 'status:claimName')
        info['size'] = self.get(data_volume_mo, 'spec:storage:resources:requests:storage')
        if info['size'] is None:
            info['size'] = self.get(data_volume_mo, 'spec:pvc:resources:requests:storage')

        info['phase'] = self.get(data_volume_mo, 'status:phase')
        info['progress'] = self.get(data_volume_mo, 'status:progress')

        info['cron'] = None
        for label_key in metadata_info['label']:
            if label_key == 'cdi.kubevirt.io/dataImportCron':
                info['cron'] = metadata_info['label'][label_key]

        info['used'] = False
        info['usage'] = []
        info['usage'].append('[pvc] %s' % (info['claim_name']))

        if info['cron'] is not None:
            info['usage'].append('[cron] %s' % (info['cron']))
            info['used'] = True

        if info['cron'] is None:
            info['cronTick'] = ''
        else:
            info['cronTick'] = '\u2713'
            info['__Output']['cronTick'] = 'Green'

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

    def add_data_volume_usage(self, data_volumes, cache_enabled=True):
        pvcs = self.get_pvcs(cache_enabled=cache_enabled)
        vms = self.get_virtual_machines(cache_enabled=cache_enabled)

        for data_volume in data_volumes:
            if vms is not None:
                for vm in vms:
                    for vm_volume in vm['volume']:
                        if vm_volume['dv_namespace'] != data_volume['info']['namespace']:
                            continue

                        if vm_volume['dv_name'] != data_volume['info']['name']:
                            continue

                        data_volume['info']['usage'].append('[vm] %s' % (vm['namespace_name']))
                        data_volume['info']['used'] = True

            if data_volume['info']['ready']:
                continue

            upload_pod = None
            for pvc in pvcs:
                if pvc['namespace'] != data_volume['info']['namespace']:
                    continue

                if pvc['owner'] is None:
                    continue

                owner_kind, owner_name = pvc['owner'].split('/')
                if owner_kind == 'PersistentVolumeClaim' and owner_name == data_volume['info']['name']:
                    data_volume['info']['usage'].append('[pvc] %s' % (pvc['namespace_name']))
                    data_volume['info']['used'] = True

                if 'cdi.kubevirt.io/storage.uploadPodName' in pvc['annotation']:
                    data_volume['info']['usage'].append('[pod] %s' % (pvc['annotation']['cdi.kubevirt.io/storage.uploadPodName']))
                    upload_pod = pvc['annotation']['cdi.kubevirt.io/storage.uploadPodName']

                if 'cdi.kubevirt.io/storage.import.importPodName' in pvc['annotation']:
                    data_volume['info']['usage'].append('[pod] %s' % (pvc['annotation']['cdi.kubevirt.io/storage.import.importPodName']))

            if upload_pod is None:
                continue

            for pvc in pvcs:
                if pvc['namespace'] != data_volume['info']['namespace']:
                    continue

                if pvc['owner'] is None:
                    continue

                owner_kind, owner_name = pvc['owner'].split('/')
                if owner_kind == 'Pod' and owner_name == upload_pod:
                    data_volume['info']['usage'].append('[pvc] %s' % (pvc['namespace_name']))
                    data_volume['info']['used'] = True

        return data_volumes

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

            if key == 'cron':
                key_found = True
                if value == 'true':
                    if data_volume_info['cron'] is None:
                        return False
                    
                if value == 'false':
                    if data_volume_info['cron'] is not None:
                        return False
                    
            if key == 'pvcs':
                key_found = True
                found = False
                for item in value.split(','):
                    if len(item.split('/')) != 2:
                        continue
                    
                    if not filter_helper.match_string(item.split('/')[0], data_volume_info['namespace']):
                        continue

                    if not filter_helper.match_string(item.split('/')[1], data_volume_info['claim_name']):
                        continue

                    found = True
                    break

                if not found:
                    return False

            if key == 'used':
                key_found = True
                if value == 'true':
                    if not data_volume_info['used']:
                        return False
                    
                if value == 'false':
                    if data_volume_info['used']:
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

        all_data_volumes = self.add_data_volume_usage(all_data_volumes, cache_enabled=cache_enabled)
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
