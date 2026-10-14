class K8sServiceAccountDelete():
    def __init__(self):
        pass

    def delete_service_account(self, namespace, name, my_output=None, wait=True):
        success, deleted = self.delete_resource(
            'ServiceAccount', 
            'v1',
            name, 
            namespace=namespace, 
            object_name='service_account',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True
        
        success = self.wait_no_service_account(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True

    def delete_namespaced_service_accounts(self, namespace, my_output=None, wait=True, skip=['builder', 'default', 'deployer']):
        service_accounts = self.get_service_accounts(object_filter=['namespace:%s' % (namespace)], cache_enabled=False)
        if service_accounts is None:
            if my_output is not None:
                my_output.error('Failed to get service accounts')
            return False

        for service_account in service_accounts:
            if service_account['name'] in skip:
                continue
            
            success = self.delete_service_account(
                service_account['namespace'],
                service_account['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True