import yaml
import copy
from lib import filter_helper
from menu.common import get_confirmation


class K8sCiliumConfigHubbleRelay():
    def __init__(self):
        pass

    def get_cilium_hubble_relay_config(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        body = {}
        body['hubble'] = {}
        body['hubble']['relay'] = filter_helper.get(cilium_config_mo, 'spec:hubble:relay')
        return body

    def is_cilium_hubble_relay_enabled(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return False
        
        return filter_helper.get(cilium_config_mo, 'spec:hubble:relay:enabled', on_error=False, on_none=False)
    
    def enable_cilium_hubble_relay(self, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        body = {}
        body['hubble'] = {}
        body['hubble']['relay'] = dict(enabled=True)
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_config['spec']['hubble']['relay'] = body['hubble']['relay']
        success = self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=False)
        if not success:
            return False
        
        if not wait:
            return True
        
        # tbd
                    
        return True

    def disable_cilium_hubble_relay(self, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        body = {}
        body['hubble'] = {}
        body['hubble']['relay'] = dict(enabled=False)
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_config['spec']['hubble']['relay'] = body['hubble']['relay']
        success = self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=False)
        if not success:
            return False
        
        if not wait:
            return True
        
        # tbd
                    
        return True