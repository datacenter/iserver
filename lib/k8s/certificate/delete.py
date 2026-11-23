class K8sCertificateDelete():
    def __init__(self):
        pass

    def delete_certificate(self, namespace, name, my_output=None, wait=True):
        success, deleted = self.delete_resource(
            'Certificate', 
            'cert-manager.io/v1',
            name, 
            namespace=namespace, 
            object_name='certificate',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True

        success = self.wait_no_certificate(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def wipe_certificates(self, my_output=None, wait=True):
        certificates_mo = self.get_certificates(return_mo=True)
        if certificates_mo is None:
            return False
        
        for certificate_mo in certificates_mo:
            success = self.delete_certificate(
                certificate_mo['metadata']['namespace'],
                certificate_mo['metadata']['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False
            
        return True