class K8sPodMetallb():
    def __init__(self):
        pass

    def is_pod_metallb(self, pod, component=None):
        if 'metadata' in pod:
            labels_mo = self.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app' in labels_mo:
                    if labels_mo['app'] == 'metallb':
                        if component is not None and self.get(labels_mo, 'component') == component or component is None:
                            return True
                    
        if 'metadata' not in pod:
            if 'app' in pod['label']:
                if pod['label']['app'] == 'metallb':
                    if component is not None and self.get(pod, 'label:component') == component or component is None:
                        return True
                            
        return False
   
    def get_metallb_pod_map(self, cache_enabled=True):
        pods = self.get_metallb_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        pod_map = {}
        for pod in pods:
            pod_map[pod['host_name']] = pod['name']

        return pod_map
    
    def get_any_metallb_pod_name(self, cache_enabled=True):
        pods = self.get_metallb_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        for pod in pods:
            if pod['running']:
                return pod['name']
            
        return None
    
    def get_metallb_pods_name(self, cache_enabled=True):
        pods = self.get_metallb_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        names = []
        for pod in pods:
            names.append(pod['name'])

        return names

    def get_metallb_pods(self, component=None, return_mo=False, cache_enabled=True):
        pods = self.get_pods(
            namespace='metallb-system',
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        metallb_pods = []
        for pod in pods:
            if not self.is_pod_metallb(pod=pod, component=component):
                continue

            pod['frr_cli'] = 'oc exec -it -n %s %s -c frr -- vtysh' % (pod['namespace'], pod['name'])
            metallb_pods.append(pod)

        if not return_mo:
            metallb_pods = sorted(
                metallb_pods,
                key=lambda i: i['host_name']
            )

        return metallb_pods

    def get_metallb_pods_exec(self, component='speaker', nodes=[], commands=[], cache_enabled=True):
        pods = self.get_pods(
            namespace='metallb-system',
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None

        metallb_pods = []
        for pod in pods:
            if not self.is_pod_metallb(pod=pod, component=component):
                continue
            
            if len(nodes) > 0 and pod['host_name'] not in nodes:
                continue

            metallb_pods.append(pod)

        metallb_pods = sorted(
            metallb_pods,
            key=lambda i: i['host_name']
        )
        
        output = {}
        for pod in metallb_pods:
            output[pod['name']] = {}
            output[pod['name']]['host'] = pod['host_name']
            for command in commands:    
                output[pod['name']][command] = self.get_pod_exec(
                    'metallb-system',
                    pod['name'],
                    ['vtysh', '-c', command],
                    container='frr'
                )            

        return output
