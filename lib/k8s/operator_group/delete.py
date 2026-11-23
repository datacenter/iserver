class K8sOperatorGroupDelete():
    def __init__(self):
        pass

    def delete_operator_group(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'OperatorGroup', 
            'operators.coreos.com/v1',
            name, 
            'operator_group',
            namespace=namespace, 
            wait=wait,
            my_output=my_output
        )
        return success
    
    def delete_operator_group_in_namespace(self, namespace, my_output=None, wait=True):
        groups = self.get_operator_groups(
            object_filter=['namespace:%s' % (namespace)],
            cache_enabled=False
        )
        for group in groups:
            success = self.delete_operator_group(
                namespace, 
                group['name'], 
                my_output=my_output, 
                wait=wait
            )
            if not success:
                return False

        return True