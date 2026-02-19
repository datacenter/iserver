import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sServiceMonitorCreate():
    def __init__(self):
        pass

    def get_service_monitor_base_body(self, namespace, name, labels=None):
        body = {}
        body['apiVersion'] = 'monitoring.coreos.com/v1'
        body['kind'] = 'ServiceMonitor'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['selector'] = {}
        body['spec']['selector']['matchLabels'] = {}
        body['spec']['endpoints'] = []

        if labels is not None:
            for key in labels:
                body['spec']['selector']['matchLabels'][key] = labels[key]

        return body
    
    def create_service_monitor(
            self, 
            namespace, 
            name, 
            body,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Service Monitor', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))            

        if self.is_service_monitor(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_service_monitor_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until service monitor found [timeout:60s]...')

        success = self.wait_service_monitor(namespace, name, max_time=360)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if my_output is not None:
            my_output.default('Wait until service monitor target ready [timeout:360s]...')

        success = self.wait_service_monitor_ready(namespace, name, max_time=360)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
        
        return True
