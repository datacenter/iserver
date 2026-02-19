import yaml
import json
from menu.common import get_confirmation


class K8sClusterwidePrivateNetworkPod():
    def __init__(self):
        pass

    def get_clusterwide_private_network_pod_body(self, namespace, name, image, network, addr4, addr6, mac, caps=False):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Pod'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['metadata']['annotations'] = {}

        annotation = {}
        annotation['network'] = network
        if addr4 is not None:
            annotation['ipv4'] = addr4
        if addr6 is not None:
            annotation['ipv6'] = addr6
        annotation['mac'] = mac
        body['metadata']['annotations']['network.v1alpha1.isovalent.com/network-attachment'] = "%s" % (json.dumps(annotation))

        images = ['netshoot']
        if image not in images:
            image = 'netshoot'

        if image == 'netshoot':
            body['spec'] = {}
            container = {}
            container['name'] = 'netshoot'
            container['image'] = 'nicolaka/netshoot:latest'
            if caps:
                container['securityContext'] = {}
                container['securityContext']['runAsUser'] = 0
                container['securityContext']['capabilities'] = {}
                container['securityContext']['capabilities']['add'] = ['IPC_LOCK', 'SYS_RESOURCE', 'NET_RAW']
                
            container['command'] = ['sleep', 'infinite']
            body['spec']['containers'] = [container]

        return body

    def create_clusterwide_private_network_pod(self, namespace, name, image, network, addr4, addr6, mac, caps=False, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create POD in Clusterwide Private Network', before_newline=True, underline=True)
            my_output.default('- network: %s' % (network))
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- image: %s' % (image))
            if addr4 is not None:
                my_output.default('- ipv4: %s' % (addr4))
            if addr6 is not None:
                my_output.default('- ipv4: %s' % (addr6))
            my_output.default('- mac: %s' % (mac))

        if self.is_pod(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- pod already exists')
            return True

        body = self.get_clusterwide_private_network_pod_body(namespace, name, image, network, addr4, addr6, mac, caps=caps)
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_resource(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Pod created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for pod running...')

            if not self.wait_pod_phase(namespace, name, ['Running'], max_time=600):
                if my_output is not None:
                    my_output.error('Pod has not reached desired running state')
                return False

        return True    
