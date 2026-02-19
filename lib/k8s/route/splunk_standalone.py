import yaml
from menu.common import get_confirmation


class K8sRouteSplunkStandalone():
    def __init__(self):
        pass

    def create_splunk_standalone_route(self, namespace, name, confirmation=False, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Create splunk instance route', before_newline=True, underline=True)
            my_output.default('- instance namespace: %s' % (namespace))
            my_output.default('- instance name: %s' % (name))
            
        if my_output is None:
            confirmation = False
        
        if not self.is_splunk_standalone(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.error('Standalone instance not found')
            return False
        
        service_namespace = namespace
        service_name = 'splunk-%s-standalone-service' % (name)
        if my_output is not None:
            my_output.default('- service namespace: %s' % (service_namespace))
            my_output.default('- service name: %s' % (service_name))

        service_mo = self.get_service(service_namespace, service_name, cache_enabled=False, return_mo=True)
        if service_mo is None:
            if my_output is not None:
                my_output.error('Service not found')
            return False

        if my_output is not None:
            my_output.default('- service found')

        route_namespace = namespace
        route_name = 'splunk-%s-standalone-service' % (name)
        if my_output is not None:
            my_output.default('- route namespace: %s' % (route_namespace))
            my_output.default('- route name: %s' % (route_name))

        if self.is_route(route_namespace, route_name):
            if my_output is not None:
                my_output.default('- route found')
            return True

        config_info = self.get_ingress_config()
        if config_info is None:
            if my_output is not None:
                my_output.error('Ingress configuration not found')
            return False
        
        body = {}
        body['apiVersion'] = 'route.openshift.io/v1'
        body['kind'] = 'Route'
        body['metadata'] = {}
        body['metadata']['namespace'] = route_namespace
        body['metadata']['name'] = route_name
        body['metadata']['labels'] = service_mo['metadata']['labels']
        body['spec'] = {}
        body['spec']['host'] = '%s-%s.%s' % (
            service_name, 
            service_namespace, 
            config_info['info']['domain']
        )
        body['spec']['port'] = {}
        body['spec']['port']['targetPort'] = 'http-splunkweb'
        body['spec']['to'] = {}
        body['spec']['to']['kind'] = 'Service'
        body['spec']['to']['name'] = service_name
        body['spec']['to']['weight'] = 100
        body['spec']['wildcardPolicy'] = None

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
            
        success = self.create_route_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('Route created', before_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for route ready...', before_newline=True)

        if not self.wait_route_ready(route_namespace, route_name):
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True

    def delete_splunk_standalone_route(self, namespace, name, my_output=None):
        if my_output is not None:
            my_output.default('Delete splunk instance route', before_newline=True, underline=True)
            my_output.default('- instance namespace: %s' % (namespace))
            my_output.default('- instance name: %s' % (name))
            
        route_namespace = namespace
        route_name = 'splunk-%s-standalone-service' % (name)
        if my_output is not None:
            my_output.default('- route namespace: %s' % (route_namespace))
            my_output.default('- route name: %s' % (route_name))

        if not self.is_route(route_namespace, route_name):
            if my_output is not None:
                my_output.default('- route already deleted')
            return True

        success = self.delete_route_mo(route_namespace, route_name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('Route deleted', before_newline=True)

        return True
    