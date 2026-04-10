class K8sOperatorGroupDelete():
    def __init__(self):
        pass

    def delete_operator_group(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'OperatorGroup', 
            'operators.coreos.com/v1',
            name, 
            namespace=namespace, 
            object_name='operator_group',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_operator_group(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True
    
    def delete_operator_group_in_namespace(self, namespace, my_output=None, wait=True):
        groups = self.get_operator_groups(
            object_filter=['namespace:%s' % (namespace)],
            cache_enabled=False
        )
        for group in groups:
            success = self.delete_operator_group(namespace, group['name'], my_output=my_output, wait=wait)
            if not success:
                return False

        return True