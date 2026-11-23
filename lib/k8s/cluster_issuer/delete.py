class K8sClusterIssuerDelete():
    def __init__(self):
        pass

    def delete_cluster_issuer(self, name, my_output=None, wait=True):
        success, deleted = self.delete_resource(
            'ClusterIssuer', 
            'cert-manager.io/v1',
            name, 
            object_name='cluster_issuer',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True

        success = self.wait_no_cluster_issuer(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True

    def wipe_cluster_issuers(self, my_output=None, wait=True):
        issuers_mo = self.get_cluster_issuers(return_mo=True)
        if issuers_mo is None:
            return False
        
        for issuer_mo in issuers_mo:
            success = self.delete_cluster_issuer(
                issuer_mo['metadata']['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False
            
        return True