class CiliumLoadBalancerIpPoolDelete():
    def __init__(self):
        pass
    
    def delete_cilium_load_balancer_ip_pool(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete LB IP Pool', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_cilium_load_balancer_ip_pool(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        success = self.delete_cilium_load_balancer_ip_pool_mo(name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no pool')

        success = self.wait_no_cilium_load_balancer_ip_pool(name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True

    def delete_cilium_load_balancer_ip_pools(self, my_output=None, wait=True, brief=False):
        managed_objects = self.get_cilium_load_balancer_ip_pool_mo(cache_enabled=False)
        if managed_objects is None:
            if my_output is not None:
                my_output.error('Failed to get CiliumLoadBalancerIPPool CRDs')
            return False
        
        if len(managed_objects) == 0 and my_output is not None:
            if my_output is not None:
                my_output.default('All CiliumLoadBalancerIPPool CRDs %s' % (my_output.add_color('already deleted', 'Green')))

        for managed_object in managed_objects:
            if brief:
                success = self.delete_cilium_load_balancer_ip_pool(
                    managed_object['metadata']['name'],
                    my_output=None, 
                    wait=wait
                )
            else:
                success = self.delete_cilium_load_balancer_ip_pool(
                    managed_object['metadata']['name'],
                    my_output=my_output, 
                    wait=wait
                )

            if success:
                if my_output is not None:
                    my_output.default('CiliumLoadBalancerIPPool %s %s' % (managed_object['metadata']['name'], my_output.add_color('deleted', 'Green')))
            else:
                if my_output is not None:
                    my_output.default('CiliumLoadBalancerIPPool %s %s' % (managed_object['metadata']['name'], my_output.add_color('delete failed', 'Red')))
                return False
            
        return True
