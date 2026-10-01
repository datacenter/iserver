import yaml
import copy
from lib import filter_helper
from menu.common import get_confirmation


class K8sCiliumConfigPrivateNetwork():
    def __init__(self):
        pass

    def is_cilium_private_network_enabled(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return False
        
        pnet_mo = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks')
        if pnet_mo is None:
            return False
        
        if not filter_helper.get(pnet_mo, 'enabled', on_error=False, on_none=False):
            return False
        
        return True

    def is_cilium_private_network_webhook_enabled(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return False
        
        enabled = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:webhook:enabled')
        if enabled is None:
            return False
        
        return enabled

    def is_cilium_private_network_multus_enabled(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return False
        
        enabled = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:networkAttachmentDefinitions:enabled')
        if enabled is None:
            return False
        
        return enabled

    def get_cilium_private_network_configuration(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        body = {}
        body['spec'] = {}
        body['spec']['enterprise'] = {}
        body['spec']['enterprise']['privateNetworks'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks')

        if body['spec']['enterprise']['privateNetworks'] is None:
            return None
        
        return body

    def is_cilium_private_network_configured(self, cache_enabled=True):
        items = self.get_clusterwide_private_networks(cache_enabled=cache_enabled)
        if items is not None:
            if len(items) > 0:
                return True

        items = self.get_private_network_endpoint_slices(cache_enabled=cache_enabled)
        if items is not None:
            if len(items) > 0:
                return True

        items = self.get_private_network_external_endpoints(cache_enabled=cache_enabled)
        if items is not None:
            if len(items) > 0:
                return True

        return False

    def get_enable_cilium_private_network_body(self):
        body = {}
        body['enterprise'] = {}
        body['enterprise']['featureGate'] = {}
        body['enterprise']['featureGate']['approved'] = ['PrivateNetworks']
        body['enterprise']['privateNetworks'] = {}
        body['enterprise']['privateNetworks']['enabled'] = True
        body['kubeProxyReplacement'] = True
        body['cni'] = {}
        body['cni']['chainingMode'] = 'none'
        return body
    
    def enable_cilium_private_network(self, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False

        body = self.get_enable_cilium_private_network_body()
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)

        ## dependencies

        cilium_config['spec']['kubeProxyReplacement'] = True
        if 'cni' in cilium_config['spec']:
            cilium_config['spec']['cni']['chainingMode'] = 'none'

        ## feature itself

        if 'enterprise' not in cilium_config['spec']:
            cilium_config['spec']['enterprise'] = {}

        if 'featureGate' not in cilium_config['spec']['enterprise']:
            cilium_config['spec']['enterprise']['featureGate'] = {}

        if 'approved' not in cilium_config['spec']['enterprise']['featureGate']:
            cilium_config['spec']['enterprise']['featureGate']['approved'] = []

        if 'PrivateNetworks' not in cilium_config['spec']['enterprise']['featureGate']['approved']:
            cilium_config['spec']['enterprise']['featureGate']['approved'].append('PrivateNetworks')

        if 'privateNetworks' not in cilium_config['spec']['enterprise']:
            cilium_config['spec']['enterprise']['privateNetworks'] = {}

        cilium_config['spec']['enterprise']['privateNetworks']['enabled'] = True

        return self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)

    def disable_cilium_private_network(self, my_output=None, confirmation=False):
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])
        if 'enterprise' in cilium_spec:
            if 'privateNetworks' in cilium_spec['enterprise']:
                del cilium_spec['enterprise']['privateNetworks']

        if 'PrivateNetworks' in filter_helper.get_attr(cilium_spec, 'enterprise:featureGate:approved', on_error=[], on_none=[]):
            cilium_spec['enterprise']['featureGate']['approved'].remove('PrivateNetworks')

        return self.update_cilium_config(cilium_spec, my_output=my_output, wait=True, confirmation=confirmation)

    def enable_cilium_private_network_webhook(self, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False

        body = {}
        body['enterprise'] = {}
        body['enterprise']['privateNetworks'] = {}
        body['enterprise']['privateNetworks']['webhook'] = {}
        body['enterprise']['privateNetworks']['webhook']['enabled'] = True
        body['enterprise']['privateNetworks']['webhook']['tls'] = {}
        body['enterprise']['privateNetworks']['webhook']['tls']['auto'] = {}
        body['enterprise']['privateNetworks']['webhook']['tls']['auto']['enabled'] = True
        body['enterprise']['privateNetworks']['webhook']['tls']['auto']['method'] = 'servingcert'
        body['enterprise']['privateNetworks']['webhook']['vms'] = {}
        body['enterprise']['privateNetworks']['webhook']['vms']['networkBinding'] = 'kubevirt-kubevirt-hyperconverged'
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)

        if 'enterprise' not in cilium_config['spec']:
            if my_output is not None:
                my_output.error('Cilium enterprise features not enabled')
            return False

        if 'featureGate' not in cilium_config['spec']['enterprise']:
            if my_output is not None:
                my_output.error('Cilium enterprise features gates not configured')
            return False

        if 'privateNetworks' not in cilium_config['spec']['enterprise']:
            if my_output is not None:
                my_output.error('Cilium enterprise private network not enabled')
            return False

        cilium_config['spec']['enterprise']['privateNetworks']['enabled'] = True
        cilium_config['spec']['enterprise']['privateNetworks']['webhook'] = {}
        cilium_config['spec']['enterprise']['privateNetworks']['webhook']['enabled'] = True
        cilium_config['spec']['enterprise']['privateNetworks']['webhook']['tls'] = {}
        cilium_config['spec']['enterprise']['privateNetworks']['webhook']['tls']['auto'] = {}
        cilium_config['spec']['enterprise']['privateNetworks']['webhook']['tls']['auto']['enabled'] = True
        cilium_config['spec']['enterprise']['privateNetworks']['webhook']['tls']['auto']['method'] = 'servingcert'
        cilium_config['spec']['enterprise']['privateNetworks']['vms'] = {}
        cilium_config['spec']['enterprise']['privateNetworks']['vms']['networkBinding'] = 'kubevirt-kubevirt-hyperconverged'
        return self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)

    def disable_cilium_private_network_webhook(self, my_output=None, confirmation=False):
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])
        if 'enterprise' in cilium_spec:
            if 'privateNetworks' in cilium_spec['enterprise']:
                if 'webhook' in cilium_spec['enterprise']['privateNetworks']:
                    del cilium_spec['enterprise']['privateNetworks']['webhook']

        return self.update_cilium_config(cilium_spec, my_output=my_output, wait=True, confirmation=confirmation)

    def enable_cilium_private_network_multus(self, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False

        body = {}
        body['enterprise'] = {}
        body['enterprise']['privateNetworks'] = {}
        body['enterprise']['privateNetworks']['networkAttachmentDefinitions'] = {}
        body['enterprise']['privateNetworks']['networkAttachmentDefinitions']['enabled'] = True
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)

        if 'enterprise' not in cilium_config['spec']:
            if my_output is not None:
                my_output.error('Cilium enterprise features not enabled')
            return False

        if 'featureGate' not in cilium_config['spec']['enterprise']:
            if my_output is not None:
                my_output.error('Cilium enterprise features gates not configured')
            return False

        if 'privateNetworks' not in cilium_config['spec']['enterprise']:
            if my_output is not None:
                my_output.error('Cilium enterprise private network not enabled')
            return False

        cilium_config['spec']['enterprise']['privateNetworks']['networkAttachmentDefinitions'] = {}
        cilium_config['spec']['enterprise']['privateNetworks']['networkAttachmentDefinitions']['enabled'] = True

        return self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)

    def get_cilium_private_network_dbs(self, db_name=None, cache_enabled=True):
        # 'privnet-external-eps',

        db_names = [
            'private-networks',
            'privnet-endpoints',
            'privnet-routes',
            'privnet-inbs',
            'privnet-mapentries',
            'privnet-subnets',
            'privnet-node-attachments'
        ]

        if db_name is not None and db_name in db_names:
            db_names = [db_name]
            
        response = self.get_cilium_agent_dbs(
            db_names,
            cache_enabled=cache_enabled,
            cast_json=True
        )
        for db_name in db_names:
            if db_name not in response:
                response['db_name'] = None
                
        return response
    