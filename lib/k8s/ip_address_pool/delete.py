class K8sIpAddressPoolDelete():
    def __init__(self):
        pass

    def delete_ip_address_pool(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'IPAddressPool', 
            'metallb.io/v1beta1',
            name, 
            namespace=namespace, 
            object_name='ip_address_pool',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_ip_address_pool(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def delete_ip_address_pools(self, my_output=None, wait=True):
        pools = self.get_ip_address_pools(
            cache_enabled=False
        )
        if pools is None:
            if my_output is not None:
                my_output.error('Failed to get ip address pools')
            return False

        if len(pools) == 0:
            if my_output is not None:
                my_output.default('IP address pools %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for pool in pools:
            success = self.delete_ip_address_pool(
                pool['namespace'],
                pool['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone