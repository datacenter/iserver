import time
import traceback


class K8sPvInfo():
    def __init__(self):
        pass

    def get_pv_pod_info(self, annotations):
        info = {}

        if 'cdi.kubevirt.io/storage.uploadPodName' not in annotations:
            info['name'] = None
            return info

        info['name'] = annotations['cdi.kubevirt.io/storage.uploadPodName']
        info['phase'] = annotations['cdi.kubevirt.io/storage.pod.phase']
        info['ready'] = annotations['cdi.kubevirt.io/storage.pod.ready']
        info['restarts'] = annotations['cdi.kubevirt.io/storage.pod.restarts']

        return info

    def get_pv_info(self, pv_mo):
        if pv_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = pv_mo['metadata']['name']
        info['access_modes'] = pv_mo['spec']['access_modes']
        info['access_modes_string'] = ','.join(
            info['access_modes']
        )
        info['capacity'] = pv_mo['spec']['capacity']
        info['phase'] = pv_mo['status']['phase']
        if info['phase'] == 'Bound':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        info['csi_driver'] = pv_mo['spec']['csi']['driver']
        info['csi_handle'] = pv_mo['spec']['csi']['volume_handle']

        return info
