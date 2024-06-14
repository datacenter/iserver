import time

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
        info['access_modes_string'] = ','.join(
            info['access_modes']
        )

        info['requested_capacity'] = self.get(pvc_mo, 'spec:resources:requests:storage')
        info['capacity'] = self.get(pvc_mo, 'status:capacity')
        info['phase'] = self.get(pvc_mo, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Bound':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        info['volume_name'] = self.get(pvc_mo, 'spec:volume_name')
        info['volume_mode'] = self.get(pvc_mo, 'spec:volume_mode')
        info['storage_class_name'] = self.get(pvc_mo, 'spec:storage_class_name')
        info['storage_provisioner'] = self.get(pvc_mo, 'metadata:annotations:volume.kubernetes.io/storage-provisioner', on_error='--')
        info['selected_node'] = self.get(pvc_mo, 'metadata:annotations:volume.kubernetes.io/selected-node', on_error='--')

        info['pod'] = self.get_pvc_pod_info(
            self.get(pvc_mo, 'metadata:annotations')
        )

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

    def get_pvcs(self, object_filter=None, pv_info=False, usage_info=False, return_mo=False, cache_enabled=True):
        all_pvcs = self.get_pvcs_info(cache_enabled=cache_enabled)
        if all_pvcs is None:
            return None

        pvcs = []

        for pvc_info in all_pvcs:
            if not self.match_pvc(pvc_info['info'], object_filter):
                continue

            if return_mo:
                pvcs.append(
                    pvc_info['mo']
                )
                continue

            if pv_info:
                pvc_pv_info = self.get_pv(
                    pvc_info['info']['volume_name'],
                    cache_enabled=cache_enabled
                )
                if pvc_pv_info is None:
                    pvc_info['info']['__Output']['volume_phase'] = 'Red'
                    pvc_info['info']['volume_phase'] = '--'
                else:
                    pvc_info['info']['__Output']['volume_phase'] = pvc_pv_info['__Output']['phase']
                    pvc_info['info']['volume_phase'] = pvc_pv_info['phase']

            if usage_info:
                pvc_info['info']['usage_pod'] = []
                pvc_info['info']['usage_vmi'] = []
                pvc_info['info']['used'] = False
                pvc_info['info']['usedTick'] = '\u2717'
                pvc_info['info']['__Output']['usedTick'] = 'Red'

                pods = self.get_pods(
                    object_filter=['pvc:%s' % (pvc_info['info']['namespace_name'])]
                )
                if pods is not None:
                    for pod in pods:
                        pvc_info['info']['usage_pod'].append(
                            pod['namespace_name']
                        )

                vmis = self.get_virtual_machine_instances(
                    object_filter=['pvc:%s' % (pvc_info['info']['namespace_name'])]
                )
                if vmis is not None:
                    for vmi in vmis:
                        pvc_info['info']['usage_vmi'].append(
                            vmi['namespace_name']
                        )

                if len(pvc_info['info']['usage_pod']) > 0 or len(pvc_info['info']['usage_vmi']) > 0:
                    pvc_info['info']['used'] = True
                    pvc_info['info']['usedTick'] = '\u2713'
                    pvc_info['info']['__Output']['usedTick'] = 'Green'

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

    def get_pvc(self, namespace, name, pv_info=False, usage_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        pvcs = self.get_pvcs(
            object_filter=object_filter,
            pv_info=pv_info,
            usage_info=usage_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pvcs is None:
            return None

        if len(pvcs) == 1:
            return pvcs[0]

        return None

    def wait_pvc_bound(self, namespace, name, max_time=60, log_error_on_timeout=True):
        start_time = int(time.time())
        while True:
            pvc_info = self.get_pvc(
                namespace,
                name,
                cache_enabled=False
            )
            if pvc_info is not None:
                if pvc_info['phase'] == 'Bound':
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_pvc_bound',
                        'Max time reached: %s/%s' % (namespace, name)
                    )
                return False

            time.sleep(5)
