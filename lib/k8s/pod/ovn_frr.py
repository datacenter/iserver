class K8sPodOvnFrr():
    def __init__(self):
        pass

    def is_pod_ovn_frr(self, pod):
        if 'metadata' in pod:
            labels_mo = self.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app' in labels_mo:
                    if labels_mo['app'] == 'frr-k8s':
                        return True
                    
        if 'metadata' not in pod:
            if 'app' in pod['label']:
                if pod['label']['app'] == 'frr-k8s':
                    return True
                            
        return False
   
    def get_ovn_frr_pod_map(self, cache_enabled=True):
        pods = self.get_ovn_frr_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        pod_map = {}
        for pod in pods:
            pod_map[pod['host_name']] = pod['name']

        return pod_map
    
    def get_any_ovn_frr_pod_name(self, cache_enabled=True):
        pods = self.get_ovn_frr_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        for pod in pods:
            if pod['running']:
                return pod['name']
            
        return None
    
    def get_ovn_frr_pods_name(self, cache_enabled=True):
        pods = self.get_ovn_frr_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        names = []
        for pod in pods:
            names.append(pod['name'])

        return names

    def get_ovn_frr_pods(self, return_mo=False, cache_enabled=True):
        pods = self.get_pods(
            namespace='openshift-frr-k8s',
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        ovn_frr_pods = []
        for pod in pods:
            if not self.is_pod_ovn_frr(pod=pod):
                continue

            pod['frr_cli'] = 'oc exec -it -n %s %s -c frr -- vtysh' % (pod['namespace'], pod['name'])
            ovn_frr_pods.append(pod)

        return ovn_frr_pods

    def get_ovn_frr_pods_exec(self, nodes=[], commands=[], cache_enabled=True):
        pods = self.get_pods(
            namespace='openshift-frr-k8s',
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        ovn_frr_pods = []
        for pod in pods:
            if not self.is_pod_ovn_frr(pod=pod):
                continue
            
            if len(nodes) > 0 and pod['host_name'] not in nodes:
                continue

            ovn_frr_pods.append(pod)

        output = {}
        for pod in ovn_frr_pods:
            output[pod['name']] = {}
            output[pod['name']]['host'] = pod['host_name']
            for command in commands:    
                output[pod['name']][command] = self.get_pod_exec(
                    'openshift-frr-k8s',
                    pod['name'],
                    ['vtysh', '-c', command],
                    container='frr'
                )            

        return output
