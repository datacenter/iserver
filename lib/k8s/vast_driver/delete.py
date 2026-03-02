class K8sVastDriverDelete():
    def __init__(self):
        pass

    def delete_vast_driver(self, namespace, name, my_output=None, wait=True):
        info = self.get_vast_driver(
            namespace,
            name,
            cache_enabled=False
        )

        success = self.delete_resource(
            'VastCSIDriver', 
            'storage.vastdata.com/v1',
            name, 
            namespace=namespace, 
            object_name='vast_driver',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_vast_driver(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        if info is None:
            return True
        
        success = self.wait_no_vast_driver_resources(
            info['resource'],
            my_output=my_output
        )

        return success            
