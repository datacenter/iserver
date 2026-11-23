import time
from lib import filter_helper


class K8sPodCiliumTimescape():
    def __init__(self):
        pass

    def is_pod_cilium_timescape(self, pod):
        if 'metadata' in pod:
            labels_mo = filter_helper.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app.kubernetes.io/name' in labels_mo:
                    if labels_mo['app.kubernetes.io/name'] == 'hubble-timescape':
                        return True
                    
        if 'metadata' not in pod:
            if 'app.kubernetes.io/name' in pod['label']:
                if pod['label']['app.kubernetes.io/name'] == 'hubble-timescape':
                    return True
                            
        return False
    
    def get_cilium_timescape_pods_name(self, cache_enabled=True):
        pods = self.get_cilium_timescape_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        names = []
        for pod in pods:
            names.append(pod['name'])

        return names

    def get_cilium_timescape_pods(self, return_mo=False, cache_enabled=False):
        pods = self.get_pods(
            namespace=self.cilium_namespace,
            service_info=True,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        cilium_pods = []
        for pod in pods:
            if not self.is_pod_cilium_timescape(pod=pod):
                continue
            cilium_pods.append(pod)

        return cilium_pods
    
    def wait_cilium_timescape_pods_ready(self, max_time=300):
        start_time = int(time.time())
        while True:
            pods = self.get_cilium_timescape_pods(cache_enabled=False)
            if pods is not None and len(pods) > 0:
                running = True
                for pod in pods:
                    if not pod['running']:
                        running = False

                if running:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)

    def wait_no_cilium_timescape_pods(self, max_time=300):
        start_time = int(time.time())
        while True:
            pods = self.get_cilium_timescape_pods(cache_enabled=False)
            if pods is not None and len(pods) == 0:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                return False

            time.sleep(5)
