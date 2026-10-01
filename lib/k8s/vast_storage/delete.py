class K8sVastStorageDelete():
    def __init__(self):
        pass

    def delete_vast_storage(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'VastStorage', 
            'storage.vastdata.com/v1',
            name, 
            'vast_storage',
            namespace=namespace, 
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success