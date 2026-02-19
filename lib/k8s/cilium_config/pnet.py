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
        
        strict_mo = filter_helper.get(cilium_config_mo, 'spec:enterprise:featureGate:strict')
        if strict_mo is None:
            return False

        if strict_mo:
            return False

        cni_mo = filter_helper.get(cilium_config_mo, 'spec:cni:chainingMode')
        if cni_mo is None:
            return False
        
        if cni_mo != 'portmap':
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

    def get_cilium_private_network_configuration(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        return  filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks')        

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
    
    def enable_cilium_private_network(self, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False

        body = {}
        body['cni'] = {}
        body['cni']['chainingMode'] = 'portmap'
        body['cni']['binPath'] = '/var/lib/cni/bin'
        body['cni']['confPath'] = '/var/run/multus/cni/net.d'
        body['cni']['exclusive'] = False
        body['enterprise'] = {}
        body['enterprise']['featureGate'] = {}
        body['enterprise']['featureGate']['strict'] = False
        body['enterprise']['privateNetworks'] = {}
        body['enterprise']['privateNetworks']['enabled'] = True
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)

        if 'enterprise' not in cilium_config['spec']:
            cilium_config['spec']['enterprise'] = {}

        if 'featureGate' not in cilium_config['spec']['enterprise']:
            cilium_config['spec']['enterprise']['featureGate'] = {}

        cilium_config['spec']['enterprise']['featureGate']['strict'] = False

        if 'privateNetworks' not in cilium_config['spec']['enterprise']:
            cilium_config['spec']['enterprise']['privateNetworks'] = {}

        cilium_config['spec']['enterprise']['privateNetworks']['enabled'] = True

        if 'cni' not in cilium_config['spec']:
            cilium_config['spec']['cni'] = {}
            cilium_config['spec']['cni']['chainingMode'] = 'portmap'
            cilium_config['spec']['cni']['binPath'] = '/var/lib/cni/bin'
            cilium_config['spec']['cni']['confPath'] = '/var/run/multus/cni/net.d'
            cilium_config['spec']['cni']['exclusive'] = False

        return self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)

    def disable_cilium_private_network(self, my_output=None, confirmation=False):
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])
        if 'enterprise' in cilium_spec:
            if 'privateNetworks' in cilium_spec['enterprise']:
                del cilium_spec['enterprise']['privateNetworks']

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

        # cilium agent reloads not expected and not required
        return self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=False)

    def disable_cilium_private_network_webhook(self, my_output=None, confirmation=False):
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])
        if 'enterprise' in cilium_spec:
            if 'privateNetworks' in cilium_spec['enterprise']:
                if 'webhook' in cilium_spec['enterprise']['privateNetworks']:
                    del cilium_spec['enterprise']['privateNetworks']['webhook']

        # cilium agent reloads not expected and not required
        return self.update_cilium_config(cilium_spec, my_output=my_output, wait=False, confirmation=confirmation)

    def get_cilium_private_network_dbs(self, cache_enabled=True):
        db_names = [
            'private-networks',
            'privnet-endpoints',
            'privnet-routes',
            'privnet-inbs',
            'privnet-mapentries',
            'privnet-external-eps'
        ]
        response = self.get_cilium_agent_dbs(
            db_names,
            cache_enabled=cache_enabled,
            cast_json=True
        )
        for db_name in db_names:
            if db_name not in response:
                response['db_name'] = None
                
        return response
    