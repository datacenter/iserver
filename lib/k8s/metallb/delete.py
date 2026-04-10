class K8sMetalLbDelete():
    def __init__(self):
        pass

    def delete_metallb(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.instance_metallb_resources,
            cache_enabled=False
        )
        
        success = self.delete_resource(
            'MetalLB', 
            'metallb.io/v1beta1',
            name, 
            namespace=namespace, 
            object_name='metallb',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_metallb(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_no_subscription_resources(
            'metallb', 
            resources, 
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def delete_metallbs(self, my_output=None, wait=True):
        instances = self.get_metallbs(
            cache_enabled=False
        )
        if instances is None:
            if my_output is not None:
                my_output.error('Failed to get metallb instances')
            return False

        if len(instances) == 0:
            if my_output is not None:
                my_output.default('Metallb instances %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for instance in instances:
            success = self.delete_metallb(
                instance['namespace'],
                instance['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone