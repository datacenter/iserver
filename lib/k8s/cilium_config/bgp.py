import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sCiliumConfigBgp():
    def __init__(self):
        pass

    def is_cilium_bgp_enabled(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return False
        
        bgp_mo = filter_helper.get(cilium_config_mo, 'spec:enterprise:bgpControlPlane')
        if bgp_mo is None:
            return False
        
        if not filter_helper.get(bgp_mo, 'enabled', on_error=False, on_none=False):
            return False
        
        return True

    def is_cilium_bgp_ready(self, cache_enabled=True):
        if not self.is_cilium_bgp_enabled(cache_enabled=cache_enabled):
            return False
        
        crds = self.get_isovalent_bgp_cluster_configs(
            cache_enabled=False
        )
        if crds is None:
            return False
        
        return True

    def get_cilium_bgp_configuration(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        return  filter_helper.get(cilium_config_mo, 'spec:enterprise:bgpControlPlane')

    def enable_cilium_bgp(self, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Enable BGP Control Plane', before_newline=True, underline=True)

        body = {}
        body['enterprise'] = {}
        body['enterprise']['bgpControlPlane'] = {}
        body['enterprise']['bgpControlPlane']['enabled'] = True
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)

        if 'enterprise' not in cilium_config['spec']:
            cilium_config['spec']['enterprise'] = {}

        if 'bgpControlPlane' not in cilium_config['spec']['enterprise']:
            cilium_config['spec']['enterprise']['bgpControlPlane'] = {}

        cilium_config['spec']['enterprise']['bgpControlPlane']['enabled'] = True

        success = self.update_cilium_config(
            cilium_config['spec'], 
            my_output=my_output, 
            confirmation=confirmation,
            wait=True
        )
        if not success:
            return False
        
        if my_output is not None:
            my_output.default('Wait for IsovalentBGPClusterConfig CRD')

        success = self.wait_isovalent_bgp_cluster_config_crd()
        if not success:
            if my_output is not None:
                my_output.error('timed out')
            return False
        
        return True

    def disable_cilium_bgp(self, my_output=None, confirmation=False, wait_for_no_crd=True):
        if my_output is not None:
            my_output.default('Disable BGP Control Plane', before_newline=True, underline=True)

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        if 'enterprise' in cilium_config['spec']:
            if 'bgpControlPlane' in cilium_config['spec']['enterprise']:
                del cilium_config['spec']['enterprise']['bgpControlPlane']

        success = self.update_cilium_config(
            cilium_config['spec'], 
            my_output=my_output, 
            confirmation=confirmation,
            wait=True
        )
        if not success:
            return False

        if not wait_for_no_crd:
            return True
        
        if my_output is not None:
            my_output.default('Wait for no IsovalentBGPClusterConfig CRD')

        success = self.wait_no_isovalent_bgp_cluster_config_crd()
        if not success:
            if my_output is not None:
                my_output.error('timed out')
            return False
        
        return True
