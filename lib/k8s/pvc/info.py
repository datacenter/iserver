import time
import traceback


class K8sPvcInfo():
    def __init__(self):
        pass

    def get_pvc_pod_info(self, annotations):
        info = {}

        if 'cdi.kubevirt.io/storage.uploadPodName' not in annotations:
            info['name'] = None
            return info

        info['name'] = annotations['cdi.kubevirt.io/storage.uploadPodName']
        info['phase'] = annotations['cdi.kubevirt.io/storage.pod.phase']
        info['ready'] = annotations['cdi.kubevirt.io/storage.pod.ready']
        info['restarts'] = annotations['cdi.kubevirt.io/storage.pod.restarts']

        return info

    def get_pvc_info(self, pvc_mo):
        info = {}
        info['__Output'] = {}

        info['name'] = pvc_mo['metadata']['name']
        info['namespace'] = pvc_mo['metadata']['namespace']
        info['access_modes'] = pvc_mo['status']['access_modes']
        info['access_modes_string'] = ''
        if isinstance(info['access_modes'], list):
            info['access_modes_string'] = ','.join(
                info['access_modes']
            )

        info['requested_capacity'] = pvc_mo['spec']['resources']['requests']['storage']
        info['capacity'] = pvc_mo['status']['capacity']
        info['phase'] = pvc_mo['status']['phase']
        if info['phase'] == 'Bound':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        info['volume_mode'] = pvc_mo['spec']['volume_mode']
        info['volume_name'] = pvc_mo['spec']['volume_name']
        info['storage_class_name'] = pvc_mo['spec']['storage_class_name']
        info['pod'] = self.get_pvc_pod_info(
            pvc_mo['metadata']['annotations']
        )

        return info
