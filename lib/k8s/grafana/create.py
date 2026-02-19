import yaml
from menu.common import get_confirmation


class K8sGrafanaCreate():
    def __init__(self):
        pass

    def get_grafana_body(self, namespace, name, username=None, password=None, route=True):
        body = {}
        body['apiVersion'] = 'grafana.integreatly.org/v1beta1'
        body['kind'] = 'Grafana'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['metadata']['labels'] = {}
        body['metadata']['labels']['dashboards'] = name
        body['metadata']['labels']['folders'] = name

        body['spec'] = {}

        if route:
            body['spec']['route'] = {}
            body['spec']['route']['spec'] = {}

        body['spec']['config'] = {}
        body['spec']['config']['log'] = {}
        body['spec']['config']['log']['mode'] = 'console'

        if username is None:
            body['spec']['config']['auth'] = {}
            body['spec']['config']['auth']['disable_login_form'] = 'true'
        else:
            body['spec']['config']['auth'] = {}
            body['spec']['config']['auth']['disable_login_form'] = 'false'
            body['spec']['config']['security'] = {}
            body['spec']['config']['security']['admin_user'] = username
            body['spec']['config']['security']['admin_password'] = password

        return body

    def create_grafana(
            self, 
            namespace, 
            name, 
            username=None,
            password=None,
            route=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Grafana Instance', before_newline=True, underline=True)

        if self.is_grafana(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        body = self.get_grafana_body(
            namespace,
            name,
            username=username,
            password=password,
            route=route
        )

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_grafana_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until grafana found [timeout:60s]...')

        success = self.wait_grafana(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if my_output is not None:
            my_output.default('Wait until grafana resources [timeout:60s]...')

        success = self.wait_grafana_resources(namespace, name, my_output=my_output)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if my_output is not None:
            my_output.default('Wait for service account...')

        success = self.wait_service_account(namespace, '%s-sa' % (name))
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if route:
            info = self.get_grafana(namespace, name, cache_enabled=False, route_info=True)
            if info is None:
                if my_output is not None:
                    my_output.error('Failed to get grafana instance [%s/%s]' % (namespace, name))
                return False

            my_output.default('Grafana instance route [%s]' % (info['route']))
    
        return True
