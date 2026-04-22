class K8sIntersightDelete():
    def __init__(self):
        pass

    def delete_intersight(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'CiscoIntersight', 
            'intersight.cisco.com/v1',
            name, 
            namespace=namespace, 
            object_name='intersight',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_intersight(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_no_subscription_intersight_instance(my_output=my_output)
        if not success:
            return False
        
        return True
    
    def delete_intersights(self, my_output=None, wait=True):
        intersights = self.get_intersights(
            cache_enabled=False
        )
        if intersights is None:
            if my_output is not None:
                my_output.error('Failed to get CiscoIntersight objects')
            return False

        if len(intersights) == 0:
            if my_output is not None:
                my_output.default('CiscoIntersight %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for intersight in intersights:
            success = self.delete_intersight(
                intersight['namespace'],
                intersight['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone