import yaml
from menu.common import get_confirmation


class CiliumLoadBalancerIpPoolCreate():
    def __init__(self):
        pass

    def get_cilium_load_balancer_ip_pool_body(
            self, 
            name,
            cidr,
            selector
        ):
        body = {}
        body['apiVersion'] = 'cilium.io/v2'
        body['kind'] = 'CiliumLoadBalancerIPPool'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['blocks'] = []
        for item in cidr:
            body['spec']['blocks'].append(
                dict(cidr=item)
            )

        if len(selector) > 0:
            body['spec']['serviceSelector'] = {}
            body['spec']['serviceSelector']['matchLabels'] = {}
            for key in selector:
                body['spec']['serviceSelector']['matchLabels'][key] = selector[key]

        return body

    def create_cilium_load_balancer_ip_pool(
            self, 
            name, 
            cidr,
            selector,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create LB IP Pool', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_resource = self.get_cilium_load_balancer_ip_pool(name, return_mo=True, cache_enabled=False)
        if current_resource is not None:
            if my_output is not None:
                my_output.default('LB IP Pool found and will be updated', before_newline=True)
        else:
            if my_output is not None:
                my_output.default('LB IP Pool not found and will be created', before_newline=True)

        body = self.get_cilium_load_balancer_ip_pool_body(
            name,
            cidr,
            selector
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if current_resource is None:
            if not self.create_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False

        if current_resource is not None:
            body['metadata']['resourceVersion'] = current_resource['metadata']['resourceVersion']
            if not self.replace_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False

        if my_output is not None:
            my_output.default('LB IP Pool configuration created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for pool...')
    
        if not self.wait_cilium_load_balancer_ip_pool(name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
