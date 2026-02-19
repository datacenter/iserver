import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sGrafanaDashboardCreate():
    def __init__(self):
        pass

    def get_grafana_dashboard_body(self, namespace, name, dashboard_selector, jbody, folder=None):
        body = {}
        body['kind'] = 'GrafanaDashboard'
        body['apiVersion'] = 'grafana.integreatly.org/v1beta1'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['instanceSelector'] = {}
        body['spec']['instanceSelector']['matchLabels'] = {}
        body['spec']['instanceSelector']['matchLabels']['dashboards'] = dashboard_selector
        if folder is not None:
            body['spec']['folder'] = folder
            
        body['spec']['json'] = jbody

        grafana_dashboard_mo = self.get_grafana_dashboard(namespace, name, cache_enabled=False, return_mo=True)
        if grafana_dashboard_mo is not None:
            body['metadata']['resourceVersion'] = self.get(grafana_dashboard_mo, 'metadata:resourceVersion')

        return body

    def create_grafana_dashboard(self, namespace, name, instance_selector, body, folder=None, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Grafana Dashboard', before_newline=True, underline=True)

        new_body = self.get_grafana_dashboard_body(
            namespace,
            name,
            instance_selector,
            body,
            folder=folder
        )

        if my_output is not None:
            my_output.default(yaml.dump(new_body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
        
        if 'resourceVersion' in new_body['metadata']:
            success = self.replace_grafana_dashboard_mo(new_body)
            if not success:
                if my_output is not None:
                    my_output.error('Grafana dashboard update failed')
                return False

            if my_output is not None:
                my_output.default('- dashboard updated')
        
            return True
        
        success = self.create_grafana_dashboard_mo(new_body)
        if not success:
            if my_output is not None:
                my_output.error('Grafana dashboard update failed')
            return False

        if my_output is not None:
            my_output.default('- dashboard created')
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait until grafana dashboard found [timeout:60s]...')

        success = self.wait_grafana_dashboard(namespace, new_body['metadata']['name'], max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
        
        return True

    def create_grafana_dashboard_from_yaml(self, namespace, instance_name, body, fixup=False, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            if fixup:
                my_output.default('Create Grafana Dashboard from YAML (with fixup)', before_newline=True, underline=True)
            else:
                my_output.default('Create Grafana Dashboard from YAML', before_newline=True, underline=True)

        new_body = body
        if fixup:
            jbody = filter_helper.get(body, 'spec:json')
            if jbody is None:
                if my_output is not None:
                    my_output.error('spec:json not found')
                return False

            if my_output is not None:
                my_output.default('- spec:json found')

            if '${PROMETHEUS}' in jbody:
                datasource_name = self.get_instance_datasource(instance_name, 'prometheus')
                if datasource_name is None:
                    if my_output is not None:
                        my_output.error('PROMETHEUS fixup requested but no prometheus datasource in instance %s' % (instance_name))
                    return False

                jbody = jbody.replace('${PROMETHEUS}', datasource_name)
                if my_output is not None:
                    my_output.default('- ${PROMETHEUS} replaced with %s' % (datasource_name))

            if '${INSTANCE}' in jbody:
                jbody = jbody.replace('${INSTANCE}', instance_name)
                if my_output is not None:
                    my_output.default('- ${INSTANCE} replaced with %s' % (instance_name))

            new_body = self.get_grafana_dashboard_body(
                namespace,
                body['metadata']['name'],
                instance_name,
                jbody
            )

        if confirmation:
            if my_output is not None:
                my_output.default(yaml.dump(new_body), before_newline=True, wrap='~~~')
            if not get_confirmation():
                return False
        
        if 'resourceVersion' in new_body['metadata']:
            success = self.replace_grafana_dashboard_mo(new_body)
            if not success:
                if my_output is not None:
                    my_output.error('Grafana dashboard update failed')
                return False

            if my_output is not None:
                my_output.default('- dashboard updated')
        
            return True
        
        success = self.create_grafana_dashboard_mo(new_body)
        if not success:
            if my_output is not None:
                my_output.error('Grafana dashboard update failed')
            return False

        if my_output is not None:
            my_output.default('- dashboard created')
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait until grafana dashboard found [timeout:60s]...')

        success = self.wait_grafana_dashboard(namespace, new_body['metadata']['name'], max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
        
        return True
