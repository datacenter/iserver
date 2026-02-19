from lib import filter_helper


class K8sServiceCiliumTimescape():
    def __init__(self):
        pass

    def is_service_cilium_timescape(self, service):
        if 'metadata' in service:
            labels_mo = filter_helper.get(service, 'metadata:labels')
            if labels_mo is not None:
                if 'app.kubernetes.io/name' in labels_mo:
                    if labels_mo['app.kubernetes.io/name'] == 'hubble-timescape':
                        return True
                    
        if 'metadata' not in service:
            if 'app.kubernetes.io/name' in service['label']:
                if service['label']['app.kubernetes.io/name'] == 'hubble-timescape':
                    return True
                            
        return False
    
    def get_cilium_timescape_services_name(self, cache_enabled=True):
        services = self.get_cilium_timescape_services(cache_enabled=cache_enabled)
        if services is None:
            return None
        
        names = []
        for service in services:
            names.append(service['name'])

        return names

    def get_cilium_timescape_services(self, return_mo=False, cache_enabled=False):
        services = self.get_services(
            object_filter=['namespace:%s' % self.cilium_namespace],
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if services is None:
            return None
        
        cilium_services = []
        for service in services:
            if not self.is_service_cilium_timescape(service=service):
                continue
            cilium_services.append(service)

        return cilium_services
    