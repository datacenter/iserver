class K8sPortworxStorageClusterDelete():
    def __init__(self):
        pass

    def delete_portworx_storage_cluster(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete storage cluster', before_newline=True, underline=True)

        info = self.get_portworx_storage_cluster(cache_enabled=False)
        if info is None:
            my_output.default('- already deleted')
            return True
        
        if not self.delete_portworx_storage_cluster_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('- rest api successful')
        
        if wait:
            if my_output is not None:
                my_output.default('- wait for no storage cluster resources...')

            if not self.wait_no_odf_cluster():
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            if my_output is not None:
                my_output.default('- wait for no storage cluster crd [timeout:60]...')

            if not self.wait_no_portworx_storage_cluster():
                if my_output is not None:
                    my_output.error('Timed out')
                return False
                    
        return True
