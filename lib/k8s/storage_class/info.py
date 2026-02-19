from lib import filter_helper


class K8sStorageClassInfo():
    def __init__(self):
        self.storage_class = None

    def get_storage_class_info(self, storage_class_mo):
        if storage_class_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_class_mo
        )
        info.update(metadata_info)

        info['volumeBindingMode'] = self.get(storage_class_mo, 'volumeBindingMode')
        info['reclaimPolicy'] = self.get(storage_class_mo, 'reclaimPolicy')
        info['provisioner'] = self.get(storage_class_mo, 'provisioner')
        info['allowVolumeExpansion'] = self.get(storage_class_mo, 'allowVolumeExpansion')
        info['reclaimPolicy'] = self.get(storage_class_mo, 'reclaimPolicy')

        info['localStorage'] = False
        lso_namespace = self.get(storage_class_mo, 'metadata:labels:local.storage.openshift.io/owner-namespace')
        if lso_namespace is not None:
            info['localStorage'] = True

        if info['provisioner'] == 'topolvm.io':
            info['lvm_fstype'] = self.get(storage_class_mo, 'parameters:csi.storage.k8s.io/fstype')
            info['lvm_device_class'] = self.get(storage_class_mo, 'topolvm.io/device-class')

        info['default'] = False
        if 'storageclass.kubernetes.io/is-default-class' in info['annotation']:
             if info['annotation']['storageclass.kubernetes.io/is-default-class'].lower() == 'true':
                  info['default'] = True

        info['defaultTick'] = ''
        if info['default']:
             info['defaultTick'] = '\u2713'
             
        return info

    def get_storage_classes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_class is not None:
                return self.storage_class

        managed_objects = self.get_storage_class_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_class = []
        for managed_object in managed_objects:
            storage_class_info = {}
            storage_class_info['info'] = self.get_storage_class_info(
                managed_object
            )
            storage_class_info['mo'] = managed_object
            self.storage_class.append(
                storage_class_info
            )

        return self.storage_class

    def match_storage_class(self, storage_class_info, storage_class_filter):
        if storage_class_filter is None or len(storage_class_filter) == 0:
            return True

        for ap_rule in storage_class_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_class_info['name']):
                    return False

            if key == 'provisioner':
                key_found = True
                if not filter_helper.match_string(value, storage_class_info['provisioner']):
                    return False

            if key == 'lso':
                key_found = True
                if value == 'true':
                    if not storage_class_info['localStorage']:
                        return False
                else:
                    if storage_class_info['localStorage']:
                        return False

            if not key_found:
                self.log.error(
                    'match_storage_class',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_classes(self, object_filter=None, pv_info=False, pvc_info=False, return_mo=False, cache_enabled=True):
        all_storage_classes = self.get_storage_classes_info(cache_enabled=cache_enabled)
        if all_storage_classes is None:
            return None

        storage_classes = []

        for storage_class_info in all_storage_classes:
            if not self.match_storage_class(storage_class_info['info'], object_filter):
                continue

            if return_mo:
                storage_classes.append(
                    storage_class_info['mo']
                )
                continue

            if pv_info:
                storage_class_info['info']['pv'] = self.get_pvs(
                    object_filter=['sc:%s' % (storage_class_info['info']['name'])],
                    cache_enabled=cache_enabled
                )
                if storage_class_info['info']['pv'] is None:
                    storage_class_info['info']['pv'] = []

                storage_class_info['info']['pv_count'] = len(storage_class_info['info']['pv'])

            if pvc_info:
                storage_class_info['info']['pvc'] = self.get_pvcs(
                    object_filter=['sc:%s' % (storage_class_info['info']['name'])],
                    cache_enabled=cache_enabled
                )
                if storage_class_info['info']['pvc'] is None:
                    storage_class_info['info']['pvc'] = []

                storage_class_info['info']['pvc_count'] = len(storage_class_info['info']['pvc'])
                
            storage_classes.append(
                storage_class_info['info']
            )

        return storage_classes

    def get_storage_class(self, name, pv_info=False, pvc_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )

        storage_classes = self.get_storage_classes(
            object_filter=object_filter,
            pv_info=pv_info,
            pvc_info=pvc_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if storage_classes is None:
            return None

        if len(storage_classes) == 1:
            return storage_classes[0]

        return None

    def get_storage_class_names(self, cache_enabled=True):
        storage_classes = self.get_storage_classes(cache_enabled=cache_enabled)
        if storage_classes is None:
            return None
        
        names = []
        for storage_class in storage_classes:
            names.append(
                storage_class['name']
            )

        names = sorted(names)
        return names
    
    def is_storage_class(self, name, cache_enabled=True):
        storage_class = self.get_storage_class(name, cache_enabled=cache_enabled)
        if storage_class is None:
            return False
        return True
