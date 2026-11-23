class K8sCertificateRequestInfo():
    def __init__(self):
        self.certificate_request = None

    def get_certificate_request_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['requester'] = self.get(managed_object, 'spec:username')
        info['issuer'] = self.get(managed_object, 'spec:issuerRef:name')
        info['issuerT'] = [
            'kind: %s' % (self.get(managed_object, 'spec:issuerRef:kind')),
            'name: %s' % (self.get(managed_object, 'spec:issuerRef:name')),
            'group: %s' % (self.get(managed_object, 'spec:issuerRef:group'))
        ]
        info = self.add_tick(
            info, 
            'Ready', 
            'True', 
            'readyTick', 
            bool_attribute='ready',
            condition=True
        )
        info = self.add_tick(
            info, 
            'Approved', 
            'True', 
            'approvedTick', 
            bool_attribute='approved',
            condition=True
        )
        return info
    
    def get_certificate_requests(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'certificate_request', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if infos is None:
            return None
        
        return infos

    def get_certificate_request(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'certificate_request', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_certificate_request(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_certificate_request(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_certificate_request(self, cache_enabled=True):
        infos = self.get_certificate_requests(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True