class K8sCertificateCreate():
    def __init__(self):
        pass

    def get_certificate_body(self, namespace, name, kind, issuer, ca=True):
        body = {}
        body['apiVersion'] = 'cert-manager.io/v1'
        body['kind'] = 'Certificate'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['commonName'] = name
        body['spec']['isCA'] = ca
        body['spec']['issuerRef'] = {}
        body['spec']['issuerRef']['group'] = 'cert-manager.io'
        body['spec']['issuerRef']['kind'] = kind
        body['spec']['issuerRef']['name'] = issuer
        body['spec']['secretName'] = name
        return body

    def create_certificate(self, namespace, name, issuer, kind='Issuer', ca=True, confirmation=False, my_output=None, wait=True):
        body = self.get_certificate_body(
            namespace,
            name,
            kind,
            issuer,
            ca=ca
        )

        success = self.create_resource_and_wait(
            body, 
            'certificate', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False
        
        if wait:
            success = self.wait_certificate(
                namespace,
                name,
                match_properties={'ready':True},
                max_time=60,
                my_output=my_output
            )
            if not success:
                return False
            
        return True