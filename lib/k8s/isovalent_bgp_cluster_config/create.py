import yaml
import json
from lib import ip_helper
from menu.common import get_confirmation


class K8sIsovalentBGPClusterConfigCreate():
    def __init__(self):
        pass

    def get_isovalent_bgp_cluster_config_body(
            self, 
            name,
            asn,
            peer,
            label
        ):
        body = {}
        body['apiVersion'] = 'isovalent.com/v1'
        body['kind'] = 'IsovalentBGPClusterConfig'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}

        if len(label) > 0:
            body['spec']['nodeSelector'] = {}
            body['spec']['nodeSelector']['matchLabels'] = {}
            for key in label:
                body['spec']['nodeSelector']['matchLabels'][key] = label[key]

        body['spec']['bgpInstances'] = []

        instance_mo = {}
        instance_mo['localASN'] = asn
        instance_mo['name'] = 'bgp'
        instance_mo['peers'] = []

        for item in peer:
            peer_mo = {}
            peer_mo['name'] = item['name']
            peer_mo['peerASN'] = int(item['asn'])
            peer_mo['peerAddress'] = item['ip']
            peer_mo['peerConfigRef'] = dict(name=item['config'])
            instance_mo['peers'].append(peer_mo)

        body['spec']['bgpInstances'].append(
            instance_mo
        )
        return body

    def create_isovalent_bgp_cluster_config(
            self, 
            name, 
            asn,
            peer,
            label,
            break_on_ref=False,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create BGP Cluster Config', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_resource = self.get_isovalent_bgp_cluster_config(name, return_mo=True, cache_enabled=False)
        if current_resource is not None:
            if my_output is not None:
                my_output.default('BGP cluster config found and will be updated', before_newline=True)
        else:
            if my_output is not None:
                my_output.default('BGP cluster config not found and will be created', before_newline=True)

        body = self.get_isovalent_bgp_cluster_config_body(
            name,
            asn,
            peer,
            label
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
            my_output.default('BGP cluster config configuration created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for crd...')
    
        if not self.wait_isovalent_bgp_cluster_config(name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
