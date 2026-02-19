import time
from lib import filter_helper


class K8sPvInfo():
    def __init__(self):
        self.pvol = None

    def get_pv_pod_info(self, annotations):
        info = {}
        info['name'] = self.get(annotations, 'cdi.kubevirt.io/storage.uploadPodName')
        info['phase'] = self.get(annotations, 'cdi.kubevirt.io/storage.pod.phase')
        info['ready'] = self.get(annotations, 'cdi.kubevirt.io/storage.pod.ready')
        info['restarts'] = self.get(annotations, 'cdi.kubevirt.io/storage.pod.restarts')
        return info

    def get_pv_info(self, pv_mo):
        if pv_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            pv_mo
        )
        info.update(metadata_info)

        info['access_modes'] = self.get(pv_mo, 'spec:access_modes', on_error=[], on_none=[])
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
            
        info['volume_mode'] = self.get(pv_mo, 'spec:volume_mode')
        info['capacity'] = self.get(pv_mo, 'spec:capacity')
        info['csi_driver'] = self.get(pv_mo, 'spec:csi:driver')
        info['csi_driverT'] = self.get(pv_mo, 'spec:csi:driver', on_error='--')
        info['csi_handle'] = self.get(pv_mo, 'spec:csi:volume_handle')
        info['csi_handleT'] = self.get(pv_mo, 'spec:csi:volume_handle', on_error='--')

        owner = self.get(pv_mo, 'metadata:labels:storage.openshift.com/owner-kind')

        info['local_volume_set'] = None
        if owner is not None and owner == 'LocalVolumeSet':
            if info['csi_driver'] is None:
                info['csi_driverT'] = 'LocalVolumeSet'
                info['csi_handleT'] = self.get(pv_mo, 'metadata:labels:storage.openshift.com/owner-name', on_error='--')
                info['local_volume_set'] = self.get(pv_mo, 'metadata:labels:storage.openshift.com/owner-name')

        info['local_volume'] = None
        if owner is not None and owner == 'LocalVolume':
            if info['csi_driver'] is None:
                info['csi_driverT'] = 'LocalVolume'
                info['csi_handleT'] = self.get(pv_mo, 'metadata:labels:storage.openshift.com/owner-name', on_error='--')
                info['local_volume'] = self.get(pv_mo, 'metadata:labels:storage.openshift.com/owner-name')

        info['device_id'] = self.get(pv_mo, 'metadata:annotations:storage.openshift.com/device-id')
        info['device_name'] = self.get(pv_mo, 'metadata:annotations:storage.openshift.com/device-mame')
        info['device_hostname'] = self.get(pv_mo, 'metadata:labels:kubernetes.io/hostname')

        info['deviceT'] = '--'
        if info['device_id'] is not None:
            info['deviceT'] = info['device_id']
        
        if info['device_hostname'] is not None:
            if info['device_id'] is None:
                info['deviceT'] = '@%s' % (info['device_hostname'])
            else:
                info['deviceT'] = '%s [%s]' % (info['deviceT'], info['device_hostname'])

        info['pvc_namespace'] = self.get(pv_mo, 'spec:claim_ref:namespace')
        info['pvc_name'] = self.get(pv_mo, 'spec:claim_ref:name')
        if info['pvc_namespace'] is None:
            info['pvc_namespace_nameT'] = '--'
        else:    
            info['pvc_namespace_nameT'] = '%s/%s' % (
                info['pvc_namespace'],
                info['pvc_name']
            )

        info['phase'] = self.get(pv_mo, 'status:phase')
        info['__Output']['phase'] = 'Red'
        if info['phase'] is not None and info['phase'] == 'Bound':
            info['__Output']['phase'] = 'Green'
        if info['phase'] is not None and info['phase'] == 'Available':
            info['__Output']['phase'] = 'Blue'

        info['storage_class'] = self.get(pv_mo, 'spec:storage_class_name')

        return info

    def match_pv(self, pv_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, pv_info['name']):
                    return False

            if key == 'sc':
                key_found = True
                if not filter_helper.match_string(value, pv_info['storage_class']):
                    return False

            if key == 'scs':
                key_found = True
                found = False
                for item in value.split(','):
                    if filter_helper.match_string(item, pv_info['storage_class']):
                        found = True

                if not found:
                    return False
                
            if key == 'local-volume':
                key_found = True
                if not filter_helper.match_string(value, pv_info['local_volume']):
                    return False

            if key == 'local-volumes':
                key_found = True
                found = False
                for item in value.split(','):
                    if filter_helper.match_string(item, pv_info['local_volume']):
                        found = True

                if not found:
                    return False
                
            if key == 'local-volume-set':
                key_found = True
                if not filter_helper.match_string(value, pv_info['local_volume_set']):
                    return False

            if key == 'local-volume-sets':
                key_found = True
                found = False
                for item in value.split(','):
                    if filter_helper.match_string(item, pv_info['local_volume_set']):
                        found = True

                if not found:
                    return False
                                                
            if key == 'pvc-namespace':
                key_found = True
                if not filter_helper.match_string(value, pv_info['pvc_namespace']):
                    return False

            if key == 'pvc-name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (pv_info['pvc_namespace'], pv_info['pvc_name'])):
                    return False

            if key == 'pvcs':
                key_found = True
                found = False
                for item in value.split(','):
                    if not filter_helper.match_string(item.split('/')[0], pv_info['pvc_namespace']):
                        continue

                    if not filter_helper.match_string(item.split('/')[1], pv_info['pvc_name']):
                        continue

                    found = True
                    break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_pv',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_pvs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.pvol is not None:
                return self.pvol

        managed_objects = self.get_pv_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.pvol = []
        for managed_object in managed_objects:
            pv_info = {}
            pv_info['info'] = self.get_pv_info(
                managed_object
            )
            pv_info['mo'] = managed_object
            self.pvol.append(
                pv_info
            )

        return self.pvol

    def get_pvs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_pvs = self.get_pvs_info(cache_enabled=cache_enabled)
        if all_pvs is None:
            return None

        pvs = []

        for pv_info in all_pvs:
            if not self.match_pv(pv_info['info'], object_filter):
                continue

            if return_mo:
                pvs.append(
                    pv_info['mo']
                )
                continue

            pvs.append(
                pv_info['info']
            )

        return pvs

    def is_pv(self, name, cache_enabled=True):
        if self.get_pv(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_pv(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        pvs = self.get_pvs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pvs is None:
            return None

        if len(pvs) == 1:
            return pvs[0]

        return None

    def wait_pv_local_volume(self, name, max_time=60, expected=1):
        start_time = int(time.time())
        while True:
            object_filter = ['local-volume:%s' % (name)]
            pvs = self.get_pvs(
                object_filter=object_filter,
                cache_enabled=False
            )
            if pvs is not None:
                if len(pvs) == expected:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_pv_local_volume',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)