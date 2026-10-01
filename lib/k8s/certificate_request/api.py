class K8sCertificateRequestApi():
    def __init__(self):
        self.certificate_request_mo = None
        self.certificate_request_namespace_mo = {}

    def get_certificate_request_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.certificate_request_mo,
            self.certificate_request_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.certificate_request_mo, self.certificate_request_namespace_mo = self.get_namespaced_resources(
            'CertificateRequest', 
            'cert-manager.io/v1', 
            self.certificate_request_mo,
            self.certificate_request_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_certificate_request_mo(self, namespace, name):
        success, _ = self.delete_resource('CertificateRequest', 'cert-manager.io/v1', name, namespace=namespace)
        return success