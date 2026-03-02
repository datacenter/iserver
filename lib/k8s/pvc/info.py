from lib import filter_helper


class K8sPvcInfo():
    def __init__(self):
        self.pvc = None

    def get_pvc_pod_info(self, annotations):
        info = {}
        info['name'] = self.get(annotations, 'cdi.kubevirt.io/storage.uploadPodName')
        info['phase'] = self.get(annotations, 'cdi.kubevirt.io/storage.pod.phase')
        info['ready'] = self.get(annotations, 'cdi.kubevirt.io/storage.pod.ready')
        info['restarts'] = self.get(annotations, 'cdi.kubevirt.io/storage.pod.restarts')
        return info

    def get_pvc_info(self, pvc_mo):
        if pvc_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            pvc_mo,
            exclude_annotations=['cdi.kubevirt.io/storage.clone.token']
        )
        info.update(metadata_info)

        info['access_modes'] = self.get(pvc_mo, 'status:access_modes', on_error=[], on_none=[])
        if len(info['access_modes']) == 0:
            info['access_modes'] = self.get(pvc_mo, 'spec:access_modes', on_error=[], on_none=[])
        info['access_modes_string'] = ','.join(
            info['access_modes']
        )

        info['access_modesT'] = []
        for item in info['access_modes']:
            if item == 'ReadWriteOnce':
                info['access_modesT'].append('RWO')
                continue

            if item == 'ReadOnlyMany':
                info['access_modesT'].append('ROM')
                continue

            if item == 'ReadWriteMany':
                info['access_modesT'].append('RWM')
                continue

            if item == 'ReadWriteOncePod':
                info['access_modesT'].append('POD')
                continue

            info['access_modesT'].append(item)

        info['requested_capacity'] = self.get(pvc_mo, 'spec:resources:requests:storage')
        info['capacity'] = self.get(pvc_mo, 'status:capacity')
        info['size'] = self.get(pvc_mo, 'status:capacity:storage')
        if info['size'] is None:
            info['size'] = self.get(pvc_mo, 'spec:resources:requests:storage')

        info['phase'] = self.get(pvc_mo, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Bound':
            info['__Output']['phase'] = 'Green'
            info['ready'] = True
        else:
            info['__Output']['phase'] = 'Red'
            info['ready'] = False

        info['volume_name'] = self.get(pvc_mo, 'spec:volume_name')
        info['volume_mode'] = self.get(pvc_mo, 'spec:volume_mode')
        info['storage_class_name'] = self.get(pvc_mo, 'spec:storage_class_name')
        info['storage_provisioner'] = self.get(pvc_mo, 'metadata:annotations:volume.kubernetes.io/storage-provisioner', on_error='--')
        info['selected_node'] = self.get(pvc_mo, 'metadata:annotations:volume.kubernetes.io/selected-node', on_error='--')

        info['pod'] = self.get_pvc_pod_info(
            self.get(pvc_mo, 'metadata:annotations')
        )

        info['cron'] = None
        for label_key in metadata_info['label']:
            if label_key == 'cdi.kubevirt.io/dataImportCron':
                info['cron'] = metadata_info['label'][label_key]

        if info['cron'] is None:
            info['cronTick'] = ''
        else:
            info['cronTick'] = '\u2713'
            info['__Output']['cronTick'] = 'Green'

        return info

    def add_pvc_info(self, info):
        info['usage'] = []
        info['dv_name'] = None
        info['dvTick'] = ''
        info['usage_pod'] = []
        info['usage_vmi'] = []
        info['used'] = False
        info['usedTick'] = '\u2717'
        info['__Output']['usedTick'] = 'Red'

        if info['cron'] is not None:
            info['usage'].append(
                '[cron] %s' % (info['cron'])
            )

        data_volumes = self.get_data_volumes(cache_enabled=True)
        if data_volumes is not None:
            for data_volume in data_volumes:
                if data_volume['namespace'] != info['namespace']:
                    continue

                if data_volume['claim_name'] != info['name']:
                    continue

                info['usage'].append(
                    '[dv] %s' % (data_volume['name'])
                )

                info['dv_name'] = data_volume['name']
                info['dvTick'] = '\u2713'
                info['__Output']['dvTick'] = 'Green'        


        pods = self.get_pods(
            object_filter=['pvc:%s' % (info['namespace_name'])],
            cache_enabled=True
        )
        if pods is not None:
            for pod in pods:
                info['usage_pod'].append(
                    pod['namespace_name']
                )
                info['usage'].append('[pod] %s' % (pod['namespace_name']))

        vmis = self.get_virtual_machine_instances(
            object_filter=['pvc:%s' % (info['namespace_name'])],
            cache_enabled=True
        )
        if vmis is not None:
            for vmi in vmis:
                info['usage_vmi'].append(
                    vmi['namespace_name']
                )
                info['usage'].append('[vmi] %s' % (vmi['namespace_name']))

        info['snapshot'] = []
        info['snapshotCount'] = 0
        info['snapshotCountT'] = '--'
        for snapshot in self.get_volume_snapshots(cache_enabled=True):
            if snapshot['namespace'] != info['namespace']:
                continue

            if snapshot['info']['pvc'] != info['name']:
                continue

            info['snapshot'].append(
                dict(
                    namespace=snapshot['namespace'],
                    name=snapshot['name'],
                    namespace_name=snapshot['namespace_name']
                )
            )

            info['usage'].append(
                '[snap] %s' % (snapshot['namespace_name'])
            )

        if len(info['snapshot']) > 0:
            info['snapshotCount'] = len(info['snapshot'])
            info['snapshotCountT'] = info['snapshotCount']

        if len(info['usage_pod']) > 0 or len(info['usage_vmi']) > 0 or len(info['snapshot']) > 0:
            info['used'] = True
            info['usedTick'] = '\u2713'
            info['__Output']['usedTick'] = 'Green'

        pvc_pv_info = self.get_pv(
            info['volume_name'],
            cache_enabled=True
        )
        if pvc_pv_info is None:
            info['__Output']['volume_phase'] = 'Red'
            info['volume_phase'] = '--'
            info['csi_handle'] = None
            info['csi_driver'] = None
        else:
            info['usage'].append(
                '[pv] %s' % (info['volume_name'])
            )

            info['__Output']['volume_phase'] = pvc_pv_info['__Output']['phase']
            info['volume_phase'] = pvc_pv_info['phase']
            info['csi_handle'] = self.get(pvc_pv_info, 'csi_handle')
            info['csi_driver'] = self.get(pvc_pv_info, 'csi_driver')

        return info

    def match_pvc(self, pvc_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, pvc_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (pvc_info['namespace'], pvc_info['name'])):
                    return False

            if key == 'sc':
                key_found = True
                if not filter_helper.match_string(value, pvc_info['storage_class_name']):
                    return False

            if key == 'cron':
                key_found = True
                if value == 'true':
                    if pvc_info['cron'] is None:
                        return False
                    
                if value == 'false':
                    if pvc_info['cron'] is not None:
                        return False

            if key == 'used':
                key_found = True
                if value == 'true':
                    if not pvc_info['used']:
                        return False
                    
                if value == 'false':
                    if pvc_info['used']:
                        return False
                                        
            if not key_found:
                self.log.error(
                    'match_pvc',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_pvcs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.pvc is not None:
                return self.pvc

        managed_objects = self.get_pvc_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.pvc = []
        for managed_object in managed_objects:
            pvc_info = {}
            pvc_info['info'] = self.get_pvc_info(
                managed_object
            )
            pvc_info['mo'] = managed_object
            self.pvc.append(
                pvc_info
            )

        self.log.k8s_mo(
            'pvc.info',
            self.pvc
        )

        return self.pvc

    def get_pvcs(self, object_filter=None, usage_info=False, return_mo=False, cache_enabled=True):
        all_pvcs = self.get_pvcs_info(cache_enabled=cache_enabled)
        if all_pvcs is None:
            return None

        pvcs = []

        if usage_info and not cache_enabled:
            self.get_pods(cache_enabled=False)
            self.get_pvs(cache_enabled=False)
            self.get_virtual_machine_instances(cache_enabled=False)
            self.get_data_volumes(cache_enabled=False)
            self.get_volume_snapshots(cache_enabled=False)

        for pvc_info in all_pvcs:
            if usage_info:
                pvc_info['info'] = self.add_pvc_info(pvc_info['info'])

            if not self.match_pvc(pvc_info['info'], object_filter):
                continue

            if return_mo:
                pvcs.append(
                    pvc_info['mo']
                )
                continue

            pvcs.append(
                pvc_info['info']
            )
            
        return pvcs

    def is_pvc(self, namespace, name, cache_enabled=True):
        if self.get_pvc(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_pvc_used(self, namespace, name, cache_enabled=True):
        pvc_info = self.get_pvc(namespace, name, usage_info=True, cache_enabled=cache_enabled)
        if pvc_info is None:
            return False
        return pvc_info['used']

    def get_pvc(self, namespace, name, usage_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        pvcs = self.get_pvcs(
            object_filter=object_filter,
            usage_info=usage_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pvcs is None:
            return None

        if len(pvcs) == 1:
            return pvcs[0]

        return None
