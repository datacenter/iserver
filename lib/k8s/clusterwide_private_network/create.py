import yaml
from lib import ip_helper
from menu.common import get_confirmation


class K8sClusterwidePrivateNetworkCreate():
    def __init__(self):
        pass

    def get_clusterwide_private_network_body(self, name, cidrv4=None, cidrv6=None, inb=None, gatewayv4=None):
        body = {}
        body['apiVersion'] = 'isovalent.com/v1alpha1'
        body['kind'] = 'ClusterwidePrivateNetwork'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['subnets'] = []
        if cidrv4 is not None:
            body['spec']['subnets'].append(
                dict(cidr=cidrv4),
            )

        if cidrv6 is not None:
            body['spec']['subnets'].append(
                dict(cidr=cidrv6),
            )

        if inb is not None:
            body['spec']['networkBridges'] = []
            for item in inb:
                body['spec']['networkBridges'].append(
                    dict(
                        cluster=item
                    )
                )

        if gatewayv4 is not None:
            route = {}
            route['destination'] = '0.0.0.0/0'
            route['gateway'] = gatewayv4
            body['spec']['routes'] = [route]
            
        return body
    
    def create_clusterwide_private_network(self, name, cidrv4=None, cidrv6=None, inb=None, gatewayv4=None, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Clusterwide Private Network', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))
            if cidrv4 is not None:
                my_output.default('- cidrv4: %s' % (cidrv4))
            if cidrv6 is not None:
                my_output.default('- cidrv6: %s' % (cidrv6))
            if inb is not None:
                my_output.default('- bridge: %s' % (','.join(inb)))
            if gatewayv4 is not None:
                my_output.default('- gateway: %s' % (gatewayv4))

        if cidrv4 is not None:
            if not ip_helper.is_valid_ipv4_cidr(cidrv4):
                if my_output is not None:
                    my_output.error('invalid v4 cidr')
                return False

        if cidrv6 is not None:
            if not ip_helper.is_valid_ipv6_cidr(cidrv6):
                if my_output is not None:
                    my_output.error('invalid v6 cidr')
                return False

        if gatewayv4 is not None:
            if not ip_helper.is_valid_ipv4_address(gatewayv4):
                if my_output is not None:
                    my_output.error('invalid v4 gateway')
                return False

        if self.is_clusterwide_private_network(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        body = self.get_clusterwide_private_network_body(
            name,
            cidrv4=cidrv4,
            cidrv6=cidrv6,
            inb=inb,
            gatewayv4=gatewayv4
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_clusterwide_private_network_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Network created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for network...')

            if not self.wait_clusterwide_private_network(name):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    
