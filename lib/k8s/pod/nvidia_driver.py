from lib import filter_helper


class K8sPodNvidiaDriver():
    def __init__(self):
        pass

    def is_pod_nvidia_driver(self, pod):
        if 'metadata' in pod:
            labels_mo = filter_helper.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app.kubernetes.io/component' in labels_mo:
                    if labels_mo['app.kubernetes.io/component'] == 'nvidia-driver':
                        return True
                    
        if 'metadata' not in pod:
            if 'app.kubernetes.io/component' in pod['label']:
                if pod['label']['app.kubernetes.io/component'] == 'nvidia-driver':
                    return True
                            
        return False

    def is_pod_nvidia_driver_toolkit(self, pod):
        if 'metadata' in pod:
            labels_mo = filter_helper.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'openshift.driver-toolkit' in labels_mo:
                    if labels_mo['openshift.driver-toolkit'] == 'true':
                        return True
                    
        if 'metadata' not in pod:
            if 'openshift.driver-toolkit' in pod['label']:
                if pod['label']['openshift.driver-toolkit'] == 'true':
                    return True
                            
        return False
    
    def get_nvidia_driver_pods(self, return_mo=False, cache_enabled=True):
        pods = self.get_pods(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        driver_pods = []
        for pod in pods:
            if not self.is_pod_nvidia_driver(pod=pod):
                continue
            if not self.is_pod_nvidia_driver_toolkit(pod=pod):
                continue
            driver_pods.append(pod)

        return driver_pods
    
    def get_nvidia_driver_pod(self, cache_enabled=True):
        pods = self.get_nvidia_driver_pods(cache_enabled=cache_enabled)
        if pods is None or len(pods) == 0:
            return None, None
        
        return pods[0]['namespace'], pods[0]['name']
    

    def get_nvidia_smi(self, options=None, cache_enabled=True):
        namespace, name = self.get_nvidia_driver_pod(cache_enabled=cache_enabled)
        if namespace is None:
            return None
        
        command = ['nvidia-smi']
        if options is not None:
            for option in options.split(' '):
                command.append(option)

        content = self.get_pod_exec(
            namespace,
            name,
            command,
            container='nvidia-driver-ctr'
        )
        return content
