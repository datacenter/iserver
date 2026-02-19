from lib import filter_helper


class K8sPodCiliumOperator():
    def __init__(self):
        pass

    def is_pod_cilium_operator(self, pod):
        if 'metadata' in pod:
            labels_mo = filter_helper.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app.kubernetes.io/name' in labels_mo:
                    if labels_mo['app.kubernetes.io/name'] == 'cilium-operator':
                        return True
                    
        if 'metadata' not in pod:
            if 'app.kubernetes.io/name' in pod['label']:
                if pod['label']['app.kubernetes.io/name'] == 'cilium-operator':
                    return True
                            
        return False
   
    def get_cilium_operator_pods(self, return_mo=False, lease=None, cache_enabled=False):
        pods = self.get_pods(
            namespace=self.cilium_namespace,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if pods is None:
            return None
        
        cilium_pods = []
        for pod in pods:
            if not self.is_pod_cilium_operator(pod=pod):
                continue
            cilium_pods.append(pod)

        if lease is not None:
            for pod in cilium_pods:
                pod['leader'] = False
                pod['leaderTick'] = ''
                if lease['identity'] is not None and pod['host_name'] in lease['identity']:
                    pod['leader'] = True
                    pod['leaderTick'] = '\u2713'

        return cilium_pods

    def get_cilium_operator_leader_logs(self, lease, cache_enabled=False):
        if lease is None:
            return None
        
        pods = self.get_cilium_operator_pods(lease=lease, cache_enabled=cache_enabled)
        for pod in pods:
            if pod['leader']:
                logs = self.get_pod_log_mo(
                    pod['namespace'],
                    pod['name'],
                    cache_enabled=False
                )
                return True, pod['namespace'], pod['name'], logs
            
        return False, None, None, None
    