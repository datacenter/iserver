import yaml
import copy
from lib import filter_helper
from menu.common import get_confirmation


class K8sCiliumConfigTimescape():
    def __init__(self):
        pass

    def get_cilium_timescape_config(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        timescape_mo = filter_helper.get(cilium_config_mo, 'spec:hubble:timescape')
        if timescape_mo is None:
            return None
        
        approved_mo = filter_helper.get(cilium_config_mo, 'spec:enterprise:featureGate:approved')
        if approved_mo is None:
            return None
        
        body = {}
        body['enterprise'] = {}
        body['enterprise']['featureGate'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:featureGate')
        body['hubble'] = filter_helper.get(cilium_config_mo, 'spec:hubble')
        return body

    def is_cilium_timescape_enabled(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return False
        
        timescape_mo = filter_helper.get(cilium_config_mo, 'spec:hubble:timescape')
        if timescape_mo is None:
            return False
        
        approved_mo = filter_helper.get(cilium_config_mo, 'spec:enterprise:featureGate:approved')
        if approved_mo is None:
            return False
        
        if 'HubbleTimescape' not in approved_mo:
            return False
        
        return True

    def is_cilium_timescape_mesh_enabled(self, cache_enabled=True):
        if not self.is_cilium_timescape_enabled(cache_enabled=cache_enabled):
            return False
        
        cilium_config_mo = self.get_cilium_config(return_mo=True)
        if cilium_config_mo is None:
            return False
        
        mesh_mo = filter_helper.get(cilium_config_mo, 'spec:hubble:timescape:clustermesh')
        if mesh_mo is None:
            return False
                
        return True

    def get_cilium_timescape_resources(self, cache_enabled=True):
        resources = {}
        resources['pod'] = self.get_cilium_timescape_pods(cache_enabled=cache_enabled)
        resources['service'] = self.get_cilium_timescape_services(cache_enabled=cache_enabled)
        resources['endpoint'] = self.get_cilium_timescape_endpoints(cache_enabled=cache_enabled)
        return resources

    def is_cilium_timescape_ready(self, resources=None, cache_enabled=True):
        if resources is None:
            resources = self.get_cilium_timescape_resources(cache_enabled=cache_enabled)

        keys = ['pod', 'service', 'endpoint']
        for key in keys:
            if resources[key] is None:
                return False
            if len(resources[key]) == 0:
                return False

        for pod in resources['pod']:
            if not pod['running']:
                return False
        
        return True
    
    def enable_cilium_timescape(self, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        body = {}
        body['enterprise'] = {}
        body['enterprise']['featureGate'] = {}
        body['enterprise']['featureGate']['approved'] = ['HubbleTimescape']
        body['hubble'] = {}
        body['hubble']['enabled'] = True
        body['hubble']['export'] = {}
        body['hubble']['export']['timescape'] = {}
        body['hubble']['export']['timescape']['tls'] = {}
        body['hubble']['export']['timescape']['tls']['mtls'] = dict(enabled=True)
        body['hubble']['relay'] = dict(enabled=False)
        body['hubble']['timescape'] = {}
        body['hubble']['timescape']['clustermesh'] = {}
        body['hubble']['timescape']['clustermesh']['primary'] = dict(namespace='')
        body['hubble']['timescape']['enabled'] = True
        body['hubble']['timescape']['ingester'] = {}
        body['hubble']['timescape']['ingester']['k8sImporter'] = dict(enabled=True)
        body['hubble']['timescape']['static'] = {}
        body['hubble']['timescape']['static']['exporter'] = dict(enabled=True)
        body['hubble']['timescape']['useStreamAPI'] = True
        body['hubble']['tls'] = dict(enabled=True)
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

        if 'approved' not in cilium_config['spec']['enterprise']['featureGate']:
            cilium_config['spec']['enterprise']['featureGate']['approved'] = []

        if 'HubbleTimescape' not in cilium_config['spec']['enterprise']['featureGate']['approved']:
            cilium_config['spec']['enterprise']['featureGate']['approved'].append(
                'HubbleTimescape'
            )

        if 'hubble' in cilium_config['spec']:
            del cilium_config['spec']['hubble']

        cilium_config['spec']['hubble'] = body['hubble']

        success = self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)
        if not success:
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for timescape pods...')
            if not self.wait_cilium_timescape_pods_ready():
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
            expected_pods_count = len(
                self.get_cilium_timescape_pods()
            )

            my_output.default('Wait for timescape endpoints...')
            if not self.wait_cilium_timescape_endpoints_ready(expected_pods_count=expected_pods_count):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True
    
    def disable_cilium_timescape(self, my_output=None, confirmation=False, wait=True):
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])
        if 'enterprise' in cilium_spec:
            if 'featureGate' in cilium_spec['enterprise']:
                if 'approved' in cilium_spec['enterprise']['featureGate']:
                    if 'HubbleTimescape' in cilium_spec['enterprise']['featureGate']['approved']:
                        new_approved = []
                        for item in cilium_spec['enterprise']['featureGate']['approved']:
                            if item != 'HubbleTimescape':
                                new_approved.append(item)

                        cilium_spec['enterprise']['featureGate']['approved'] = new_approved

            if 'hubble' in cilium_spec:
                del cilium_spec['hubble']

        success = self.update_cilium_config(cilium_spec, my_output=my_output, wait=True, confirmation=confirmation)
        if not success:
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for no timescape pods...')
            if not self.wait_no_cilium_timescape_pods():
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            my_output.default('Wait for no timescape endpoints...')
            if not self.wait_no_cilium_timescape_endpoints():
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True
    
    def enable_cilium_timescape_mesh(self, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        body = {}
        body['hubble'] = {}
        body['hubble']['timescape'] = {}
        body['hubble']['timescape']['clustermesh'] = {}
        body['hubble']['timescape']['clustermesh']['primary'] = dict(namespace='')
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_config['spec']['hubble']['timescape']['clustermesh'] = body['hubble']['timescape']['clustermesh']

        success = self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)
        if not success:
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for timescape pods...')
            if not self.wait_cilium_timescape_pods_ready():
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
            expected_pods_count = len(
                self.get_cilium_timescape_pods()
            )

            my_output.default('Wait for timescape endpoints...')
            if not self.wait_cilium_timescape_endpoints_ready(expected_pods_count=expected_pods_count):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True
    
    def disable_cilium_timescape_mesh(self, my_output=None, confirmation=False, wait=True):
        if not self.is_cilium_timescape_mesh_enabled(cache_enabled=False):
            return True
        
        if my_output is None:
            confirmation = False

        body = {}
        body['hubble'] = {}
        body['hubble']['timescape'] = {}
        body['hubble']['timescape']['clustermesh'] = {}
        body['hubble']['timescape']['clustermesh']['primary'] = dict(namespace='')
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        del cilium_config['spec']['hubble']['timescape']['clustermesh']

        success = self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True)
        if not success:
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for timescape pods...')
            if not self.wait_cilium_timescape_pods_ready():
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
            expected_pods_count = len(
                self.get_cilium_timescape_pods()
            )

            my_output.default('Wait for timescape endpoints...')
            if not self.wait_cilium_timescape_endpoints_ready(expected_pods_count=expected_pods_count):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True
    