class CiliumLoadBalancerIpPoolWait():
    def __init__(self):
        pass

    def wait_wait_cilium_load_balancer_ip_pool(self, name, match_properties={}, break_properties={}, my_output=None, prompt='CiliumLoadBalancerIPPool', max_time=360):
        return self.wait_managed_object(
            'wait_cilium_load_balancer_ip_pool',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_wait_cilium_load_balancer_ip_pool(self, name, my_output=None, prompt='CiliumLoadBalancerIPPool', max_time=360):
        return self.wait_no_managed_object(
            'wait_cilium_load_balancer_ip_pool',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )