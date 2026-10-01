class K8sVastClusterDelete():
    def __init__(self):
        pass

    def delete_vast_cluster(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'VastCluster', 
            'storage.vastdata.com/v1',
            name, 
            'vast_cluster',
            namespace=namespace, 
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success