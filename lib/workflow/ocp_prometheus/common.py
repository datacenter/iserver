import json
import yaml
import copy
from lib import filter_helper
from lib.workflow.ocp_access import check as ocp_check


def get_default_params():
    params = {}
    params['mon-namespace'] = 'openshift-monitoring'
    params['mon-name'] = 'cluster-monitoring-config'
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

