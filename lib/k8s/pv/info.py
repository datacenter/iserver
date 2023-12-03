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

        info['volume_mode'] = self.get(pv_mo, 'spec:volume_mode')
        info['capacity'] = self.get(pv_mo, 'spec:capacity')
        info['csi_driver'] = self.get(pv_mo, 'spec:csi:driver', on_error='--')
        info['csi_handle'] = self.get(pv_mo, 'spec:csi:volume_handle', on_error='--')

        info['pvc_namespace'] = self.get(pv_mo, 'spec:claim_ref:namespace')
        info['pvc_name'] = self.get(pv_mo, 'spec:claim_ref:name')

        info['phase'] = self.get(pv_mo, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Bound':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

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

            if key == 'pvc-namespace':
                key_found = True
                if not filter_helper.match_string(value, pv_info['pvc_namespace']):
                    return False

            if key == 'pvc-name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (pv_info['pvc_namespace'], pv_info['pvc_name'])):
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
