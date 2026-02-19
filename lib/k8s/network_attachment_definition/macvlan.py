import yaml
import json
from lib import ip_helper
from menu.common import get_confirmation


class K8sNetworkAttachmentDefinitionMacVlan():
    def __init__(self):
        pass

    def get_nad_macvlan_body(self, namespace, name, master, mode, ipam, address, gateway):
        body = {}
        body['apiVersion'] = 'k8s.cni.cncf.io/v1'
        body['kind'] = 'NetworkAttachmentDefinition'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}

        config = {}
        config['cniVersion'] = '0.3.1'
        config['type'] = 'macvlan'
        config['master'] = master
        config['mode'] = mode
        config['ipam'] = {}

        if ipam == 'dhcp':
            config['ipam']['type'] = 'dhcp'

        if ipam == 'static':
            config['ipam']['type'] = 'static'
            config['ipam']['addresses'] = []

            for index in range(0, len(address.split(','))):
                address_mo = {}
                address_mo['address'] = '%s/%s' % (
                    address.split(',')[index],
                    gateway.split(',')[index].split('/')[1]
                )
                address_mo['gateway'] = gateway.split(',')[index].split('/')[0]
                config['ipam']['addresses'].append(address_mo)
        
        if ipam == 'local':
            config['ipam']['type'] = 'host-local'
            config['ipam']['subnet'] = '%s/%s' % (
                ip_helper.get_network_ipv4_in_cidr(gateway),
                gateway.split('/')[1]
            )
            config['ipam']['rangeStart'] = address.split('-')[0]
            config['ipam']['rangeEnd'] = address.split('-')[1]
            config['ipam']['gateway'] = gateway.split('/')[0]

        body['spec']['config'] = json.dumps(config, indent=2)
        return body

    def create_nad_macvlan(
            self, 
            namespace, 
            name, 
            master,
            mode,
            ipam,
            address,
            gateway,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create MacVLAN NAD', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- master: %s' % (master))
            my_output.default('- mode: %s' % (mode))
            my_output.default('- ipam: %s' % (ipam))
            if address is not None:
                my_output.default('- address: %s' % (address))
            if gateway is not None:
                my_output.default('- gateway: %s' % (gateway))

        if not self.is_namespace(namespace):
            if my_output is not None:
                my_output.error('namespace not found')
            return False
        
        if self.is_nad(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        body = self.get_nad_macvlan_body(
            namespace, 
            name, 
            master,
            mode,
            ipam,
            address,
            gateway
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_nad_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Network attachment definition created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for nad...')
    
        if not self.wait_nad(namespace, name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
