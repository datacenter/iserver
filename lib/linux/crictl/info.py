import json
from lib import filter_helper


class LinuxCrictlInfo():
    def __init__(self):
        self.crictl_ps = None

    def get_crictl_process_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['state'] = filter_helper.get(managed_object, 'state')
        info['running'] = False
        info['runningTick'] = '\u2717'
        info['__Output']['runnintTick'] = 'Red'

        info['stateT'] = info['state']
        if info['state'] is not None:
            if info['state'] == 'CONTAINER_RUNNING':
                info['stateT'] = 'running'
                info['__Output']['stateT'] = 'Green'
                info['running'] = True
                info['runningTick'] = '\u2713'

            if info['state'] == 'CONTAINER_EXITED':
                info['stateT'] = 'exited'
                info['__Output']['stateT'] = 'Yellow'

        info['name'] = filter_helper.get(managed_object, 'metadata:name')
        info['pod_namespace'] = filter_helper.get(managed_object, 'labels:io.kubernetes.pod.namespace')
        info['pod_name'] = filter_helper.get(managed_object, 'labels:io.kubernetes.pod.name')
        info['pod_restart'] = filter_helper.get(managed_object, 'annotations:io.kubernetes.container.restartCount')
        
        try:
            info['id'] = filter_helper.get(managed_object, 'id')[:13]
        except BaseException:
            info['id'] = None
        
        try:
            info['image'] = filter_helper.get(managed_object, 'image:image').split(':')[1][:13]
        except BaseException:
            info['image'] = None
        
        try:
            info['pod_id'] = filter_helper.get(managed_object, 'podSandboxId')[:13]
        except BaseException:
            info['pod_id'] = None

        return info

    def get_crictl_processes_info(self, cache_enabled=True):
        if cache_enabled and self.crictl_ps is not None:
            return self.crictl_ps

        try:
            managed_objects = json.loads(
                self.get_critctl_ps_cmd(cache_enabled=cache_enabled)
            )['containers']
        except BaseException:
            self.log.error(
                'get_crictl_processes_info',
                'Commands output parsing failed'
            )
            return None
        
        self.crictl_ps = []
        for managed_object in managed_objects:
            self.crictl_ps.append(
                self.get_crictl_process_info(
                    managed_object
                )
            )

        self.crictl_ps = sorted(
            self.crictl_ps,
            key=lambda i: i['name']
        )
        return self.crictl_ps
    
    def get_crictl_processes(self, cache_enabled=True):
        processes = self.get_crictl_processes_info(cache_enabled=cache_enabled)
        return processes
