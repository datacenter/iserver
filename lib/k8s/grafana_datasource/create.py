import yaml
from menu.common import get_confirmation


class K8sGrafanaDatasourceCreate():
    def __init__(self):
        pass

    def get_grafana_datasource_thanos_body(self, namespace, name, datasource_name, token, instance_name):
        body = {}
        body['apiVersion'] = 'grafana.integreatly.org/v1beta1'
        body['kind'] = 'GrafanaDatasource'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name

        body['spec'] = {}

        body['spec']['datasource'] = {}
        body['spec']['datasource']['access'] = 'proxy'
        body['spec']['datasource']['editable'] = True
        body['spec']['datasource']['isDefault'] = True
        body['spec']['datasource']['jsonData'] = {}
        body['spec']['datasource']['jsonData']['httpHeaderName1'] = 'Authorization'
        body['spec']['datasource']['jsonData']['timeInterval'] = '5s'
        body['spec']['datasource']['jsonData']['tlsSkipVerify'] = True
        body['spec']['datasource']['name'] = datasource_name

        body['spec']['datasource']['secureJsonData'] = {}
        body['spec']['datasource']['secureJsonData']['httpHeaderValue1'] = 'Bearer %s' % (token)

        body['spec']['datasource']['type'] = 'prometheus'
        body['spec']['datasource']['url'] = 'https://thanos-querier.openshift-monitoring.svc.cluster.local:9091'

        body['spec']['instanceSelector'] = {}
        body['spec']['instanceSelector']['matchLabels'] = {}
        body['spec']['instanceSelector']['matchLabels']['dashboards'] = instance_name

        return body

    def create_grafana_datasource_thanos(self, namespace, instance_name, datasource_name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Grafana Datasource', before_newline=True, underline=True)
            my_output.default('- instance: %s' % (instance_name))
        
        instance_info = self.get_grafana(namespace, instance_name, cache_enabled=False)
        if instance_info is None:
            if my_output is not None:
                my_output.error('Grafana instance not found')
            return False
        
        ds_name = self.get_instance_datasource(instance_name, 'prometheus')
        if ds_name is not None:
            if my_output is not None:
                my_output.default('- prometheus data source already defined: %s' % (ds_name))
            return True
        
        if my_output is not None:
            my_output.default('- get service account token for grafana instance')

        sa_namespace = instance_info['namespace']
        sa_name = '%s-sa' % (instance_name)
        token = self.get_service_account_token(
            sa_namespace,
            sa_name
        )
        if token is None:
            if my_output is not None:
                my_output.error('Failed to get service account token')
            return False

        grafana_datasource_namespace = instance_info['namespace']
        grafana_datasource_name = '%s-thanos' % (instance_info['name'])
        body = self.get_grafana_datasource_thanos_body(
            grafana_datasource_namespace,
            grafana_datasource_name,
            datasource_name, 
            token, 
            instance_name
        )

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_grafana_datasource_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if wait:
            if my_output is not None:
                my_output.default('Wait until grafana found...')

            success = self.wait_grafana_datasource(grafana_datasource_namespace, grafana_datasource_name)
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')                
                return False

            if my_output is not None:
                my_output.default('Wait until grafana datasource %s/%s in instance %s...' % (grafana_datasource_namespace, grafana_datasource_name, instance_name))

            success = self.wait_grafana_datasource_in_instance(grafana_datasource_namespace, grafana_datasource_name, instance_name)
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')                
                return False

        if my_output is not None:
            my_output.default('Grafana datasource created', before_newline=True)
            my_output.default('- %s/%s' % (grafana_datasource_namespace, grafana_datasource_name))
            my_output.default('- type: prometheus')
            my_output.default('- name: %s' % (datasource_name))
            my_output.default('- token: service account [%s/%s]' % (sa_namespace, sa_name))
            my_output.default('- dashboards: %s' % (instance_name))

        return True
    