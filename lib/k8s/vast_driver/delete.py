class K8sVastDriverDelete():
    def __init__(self):
        pass

    def delete_vast_driver(self, namespace, name, my_output=None, wait=True):
        info = self.get_vast_driver(
            namespace,
            name,
            cache_enabled=False
        )

        if info is not None:
            for resource in info['resource']:
                resource['resources'] = None

                if resource['kind'] == 'Deployment':
                    resource['resources'] = self.get_deployment_resources(
                        resource['namespace'],
                        resource['name'],
                        cache_enabled=False
                    )

                if resource['kind'] == 'DaemonSet':
                    resource['resources'] = self.get_daemon_set_resources(
                        resource['namespace'],
                        resource['name'],
                        cache_enabled=False
                    )

        success = self.delete_resource_and_wait(
            'VastCSIDriver', 
            'storage.vastdata.com/v1',
            name, 
            'vast_driver',
            namespace=namespace, 
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        if not success:
            return False

        if not wait:
            return True
        
        if info is None:
            return True
        
        success = self.wait_no_vast_driver_resources(
            info['resource'],
            my_output=my_output
        )

        return success            