import yaml
import copy
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sCiliumConfigUpdate():
    def __init__(self):
        pass

    def update_cilium_config(self, spec, my_output=None, rollback=True, wait=True, confirmation=False, restart_operator=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Cilium config update', before_newline=True, underline=True)

        cilium_config_mo = self.get_cilium_config(cache_enabled=False, return_mo=True)
        if cilium_config_mo is None:
            if my_output is not None:
                my_output.error('Failed to get CiliumConfig CRD')
            return False

        if wait:
            pods_before = self.get_cilium_agent_pods_name(cache_enabled=False)
            if pods_before is None:
                if my_output is not None:
                    my_output.error('Failed to get pods in cilium namespace')
                return False

        body = {}
        body['apiVersion'] = cilium_config_mo['apiVersion']
        body['kind'] = cilium_config_mo['kind']
        body['metadata'] = {}
        body['metadata']['name'] = cilium_config_mo['metadata']['name']
        body['metadata']['labels'] = cilium_config_mo['metadata']['labels']
        body['metadata']['resourceVersion'] = cilium_config_mo['metadata']['resourceVersion']
        body['spec'] = copy.deepcopy(spec)

        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')
            if confirmation:
                if not get_confirmation():
                    return False
                
        success = self.replace_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('CiliumConfig CRD patched')

        if not wait:
            return True

        if my_output is not None:
            my_output.default('Take a nap to check cilium config state and detect automatic deployment restart...')

        time.sleep(60)
        
        cilium_config_info = self.get_cilium_config(cache_enabled=False)
        if cilium_config_info is None:
            if my_output is not None:
                my_output.error('failed to get cilium configuration')
            return False
        
        if cilium_config_info['valid']:
            if my_output is not None:
                my_output.default('Cilium configuration valid')

        rolled_back = False

        if not cilium_config_info['valid']:
            if my_output is not None:
                my_output.error('cilium configuration invalid')
                if cilium_config_info['values_error']:
                     my_output.default('- values [reason:%s]' % (cilium_config_info['values_error_reason']))
                     my_output.default(cilium_config_info['values_error_message'], wrap='~~~')

                if cilium_config_info['processing_error']:
                     my_output.default('- processing [reason:%s]' % (cilium_config_info['processing_error_reason']))
                     my_output.default(cilium_config_info['processing_error_message'], wrap='~~~')
            
            if not rollback:
                return False
            
            if my_output is not None:
                my_output.default('Rollback to previous configuration')

            body = {}
            body['apiVersion'] = cilium_config_mo['apiVersion']
            body['kind'] = cilium_config_mo['kind']
            body['metadata'] = {}
            body['metadata']['name'] = cilium_config_mo['metadata']['name']
            body['metadata']['labels'] = cilium_config_mo['metadata']['labels']
            body['metadata']['resourceVersion'] = cilium_config_info['resource_version']
            body['spec'] = copy.deepcopy(cilium_config_mo['spec'])

            success = self.replace_resource(body)
            if not success:
                if my_output is not None:
                    my_output.error('rest api failed')
                return False
            
            rolled_back = True

            if my_output is not None:
                my_output.default('CiliumConfig CRD patched')
                my_output.default('Extra nap...')

            time.sleep(60)

        pods_after = self.get_cilium_agent_pods_name(cache_enabled=False)
        if pods_after is None:
            if my_output is not None:
                my_output.error('Failed to get agent pods in cilium namespace')
            return False

        restart_agents = False
        if not filter_helper.compare_list(pods_before, pods_after):
            if my_output is not None:
                my_output.default('Automatic agent pods rollout detected')
        else:        
            if my_output is not None:
                my_output.default('Forced agent reload')
            restart_agents = True

        if restart_agents or restart_operator:
            if restart_operator:
                if my_output is not None:
                    my_output.default('Forced operator reload')
            
            if not self.restart_cilium(my_output=my_output, wait=False, agent=restart_agents, operator=restart_operator):
                return False

            time.sleep(30)

        if not self.wait_cilium_resources(my_output=my_output):
            return False
    
        return not rolled_back

    def restart_cilium(self, agent=True, operator=True, my_output=None, wait=True):
        if operator:
            if not self.restart_deployment(self.cilium_namespace, self.cilium_operator, my_output=my_output):
                return False

        if agent:
            if not self.restart_daemon_set(self.cilium_namespace, self.cilium_agent, my_output=my_output):
                return False

        if not wait:
            return True
        
        time.sleep(60)

        if not self.wait_cilium_resources(my_output=my_output):
            return False
        
        return True
    
    def wait_cilium_resources(self, my_output=None):
        if my_output is not None:
            my_output.default('Wait for Cilium resources', before_newline=True, underline=True)

        time.sleep(10)

        deployments = self.get_deployments(
            object_filter=['namespace:%s' % (self.cilium_namespace)],
            cache_enabled=False
        )
        if deployments is None:
            if my_output is not None:
                my_output.error('Failed to get deployments')
            return False
        
        if len(deployments) == 0:
            if my_output is not None:
                my_output.error('Unexpected no deployments in cilium namespace')
            return False
        
        pods = self.get_pods(
            object_filter=['namespace:%s' % (self.cilium_namespace)],
            cache_enabled=False
        )
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to get pods')
            return False
        
        if len(pods) == 0:
            if my_output is not None:
                my_output.error('Unexpected no pods in cilium namespace')
            return False
        
        for pod in pods:
            if my_output is not None:
                my_output.default('- pod: %s' % (pod['name']))

            success = self.wait_pod_phase(
                self.cilium_namespace, 
                pod['name'], 
                'Running', 
                max_time=900
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        for deployment in deployments:
            if my_output is not None:
                my_output.default('- deployment: %s' % (deployment['name']))

            success = self.wait_deployment_ready_state(
                self.cilium_namespace, 
                deployment['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        return True
