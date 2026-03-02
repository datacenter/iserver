class K8sVastStorageDelete():
    def __init__(self):
        pass

    def delete_vast_storage(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'VastStorage', 
            'storage.vastdata.com/v1',
            name, 
            namespace=namespace, 
            object_name='vast_storage',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_vast_storage(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
