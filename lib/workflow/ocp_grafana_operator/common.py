import json
import yaml
import copy
from lib import filter_helper
from lib.workflow.ocp_access import check as ocp_check


def get_default_params():
    params = {}
    params['namespace'] = 'grafana-operator'
    params['name'] = 'grafana-operator'
    params['operator-group-name'] = 'grafana-operator-group'
    params['mon-namespace'] = 'openshift-monitoring'
    params['mon-name'] = 'cluster-monitoring-config'
    params['delete-namespace'] = True
    params['title'] = 'OpenShift Workflow - Grafana Operator'
    return params


def check_user_workload_monitoring(params, my_output):
    my_output.default('Check User Workload Monitoring', before_newline=True, underline=True)
    my_output.default('- config map namespace: %s' % (params['__default__']['mon-namespace']))
    my_output.default('- config map name: %s' % (params['__default__']['mon-name']))

    config_map_mo = params['k8s_handler'].get_config_map(
        params['__default__']['mon-namespace'], 
        params['__default__']['mon-name'], 
        cache_enabled=False, 
        return_mo=True
    )
    if config_map_mo is None:
        my_output.default('- not found <=> user workload monitoring disabled')
        return False

    data_mo = filter_helper.get(config_map_mo, 'data:config.yaml')
    if data_mo is None:
        my_output.error('Unsupported config map body')
        my_output.default(config_map_mo, before_newline=True, wrap='~~~')
        return False

    try:
        data_json = yaml.safe_load(data_mo)
    except BaseException:
        my_output.error('Unexpected failure in yaml to json cast of cm data')
        return False

    if 'enableUserWorkload' not in data_json or not data_json['enableUserWorkload']:
        my_output.default('- enableUserWorkload disabled')
        return False
    
    my_output.default('- enableUserWorkload enabled')
    return True


def get_resources(params, my_output):
    my_output.default('Collect resources', before_newline=True)

    my_output.default('- grafana')
    params['grafana'] = params['k8s_handler'].get_grafanas(datasource_info=True, route_info=True, cache_enabled=False)
    if params['grafana'] is None:
        my_output.error('grafana rest api failed')
        return None

    my_output.default('- dashboard')
    params['dashboard'] = params['k8s_handler'].get_grafana_dashboards(cache_enabled=False)
    if params['dashboard'] is None:
        my_output.error('dashboard rest api failed')
        return None
    
    my_output.default('- folder')
    params['folder'] = params['k8s_handler'].get_grafana_folders(cache_enabled=False)
    if params['folder'] is None:
        my_output.error('folder rest api failed')
        return None
    
    my_output.default('- datasource')
    params['datasource'] = params['k8s_handler'].get_grafana_datasources(cache_enabled=False)
    if params['datasource'] is None:
        my_output.error('datasource rest api failed')
        return None
    
    return params
