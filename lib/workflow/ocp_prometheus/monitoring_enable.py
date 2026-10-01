import yaml
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_prometheus import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def edit_config_map(params, config_map_mo, my_output):
    data_mo = filter_helper.get(config_map_mo, 'data:config.yaml')
    if data_mo is None:
        my_output.error('Unsupported config map body')
        my_output.default(config_map_mo, before_newline=True, wrap='~~~')
        return False, False

    try:
        data_json = yaml.safe_load(data_mo)
    except BaseException:
        my_output.error('Unexpected failure in yaml to json cast of cm data')
        return False, False

    if 'enableUserWorkload' in data_json and data_json['enableUserWorkload']:
        my_output.default('- enableUserWorkload already enabled')
        return True, False

    my_output.default('- enableUserWorkload value will be changed in config map')

    try:
        all_data_json = filter_helper.get(config_map_mo, 'data')
        config_data = yaml.safe_load(filter_helper.get(config_map_mo, 'data:config.yaml'))
        config_data['enableUserWorkload'] = True
        all_data_json['config.yaml'] = yaml.dump(config_data)
    except BaseException:
        my_output.error('Exception: config map data change failed')
        return False, False

    success = params['k8s_handler'].update_config_map(
        params['__default__']['mon-namespace'],
        params['__default__']['mon-name'],
        all_data_json,
        confirmation=params['confirmation'],
        my_output=my_output
    )
    if not success:
        return False, False
    
    return True, True


def create_config_map(params, my_output):
    data = {}
    data['config.yaml'] = 'enableUserWorkload: true\n'
    success = params['k8s_handler'].create_config_map(
        params['__default__']['mon-namespace'],
        params['__default__']['mon-name'],
        data,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    return success


def enable_user_workload_monitoring(params, my_output):
    my_output.default('Config Map', before_newline=True, underline=True)
    my_output.default('- namespace: %s' % (params['__default__']['mon-namespace']))
    my_output.default('- name: %s' % (params['__default__']['mon-name']))

    config_map_mo = params['k8s_handler'].get_config_map(
        params['__default__']['mon-namespace'], 
        params['__default__']['mon-name'], 
        cache_enabled=False, 
        return_mo=True
    )
    if config_map_mo is None:
        my_output.default('- not found and will be created')
        changed = True
        success = create_config_map(params, my_output)
        if not success:
            return False
    else:
        my_output.default('- found and will be checked')
        success, changed = edit_config_map(params, config_map_mo, my_output)
        if not success:
            return False

    if changed:
        my_output.default('Check for resources', before_newline=True, underline=True)
        success = params['k8s_handler'].wait_prometheus_user_workload_monitoring(my_output=my_output)

    return success


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Enable user-workload monitoring')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    if not enable_user_workload_monitoring(params, my_output):
        return False
    
    my_output.default('')
    my_output.default('Completed tasks', underline=True, before_newline=True)
    my_output.default('- User workload monitoring enabled')
    
    return True
