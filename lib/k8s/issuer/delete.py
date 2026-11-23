class K8sIssuerDelete():
    def __init__(self):
        pass

    def delete_issuer(self, namespace, name, my_output=None, wait=True):
        success, deleted = self.delete_resource(
            'Issuer', 
            'cert-manager.io/v1',
            name, 
            namespace=namespace, 
            object_name='issuer',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True

        success = self.wait_no_issuer(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True

    def wipe_issuers(self, my_output=None, wait=True):
        issuers_mo = self.get_issuers(return_mo=True)
        if issuers_mo is None:
            return False
        
        for issuer_mo in issuers_mo:
            success = self.delete_issuer(
                issuer_mo['metadata']['namespace'],
                issuer_mo['metadata']['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False
            
        return True