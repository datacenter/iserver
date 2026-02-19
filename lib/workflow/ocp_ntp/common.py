from lib.workflow import ocp_common
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['ssh-required'] = True
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['linux_handler'] = ocp_common.get_nodes_linux_handler(
        params['cluster'],
        params['k8s_handler'],
        log_id=log_id
    )
    if params['linux_handler'] is None:
        my_output.error('Linux access required')
        return None
    
    params['ssh-ready'] = False
    if 'ssh_public_key' in ocp_check_params['data']:
        params['ssh-ready'] = True

    return params


def get_default_params():
    params = {}
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params

def get_ocp_chrony_mc(handler):
    info = []

    machine_configs = handler.get_machine_configs(
        object_filter=['path:/etc/chrony.conf']
    )
    for machine_config in machine_configs:
        if len(machine_config['file']) == 0:
            continue

        if machine_config['name'].startswith('rendered-'):
            continue

        info.append(
            machine_config
        )

    return info


def get_ocp_chrony_config(handlers):
    info = []

    for handler in handlers:
        item = {}
        item['name'] = handlers[handler].ocp_node_name
        item['ip'] = handlers[handler].management_ip

        chrony_config = handlers[handler].get_chrony_config_info()
        if chrony_config is None:
            continue

        item['config'] = chrony_config['configuration']
        info.append(item)

    return info


def get_ocp_chrony_state(handlers):
    info = []

    for handler in handlers:
        item = {}
        item['name'] = handlers[handler].ocp_node_name
        item['ip'] = handlers[handler].management_ip

        chrony_state = handlers[handler].get_chrony_tracking_info()
        if chrony_state is None:
            continue

        for key in chrony_state:
            item[key] = chrony_state[key]

        info.append(item)

    return info


def get_ocp_chrony_info(k8s_handler, linux_handlers):
    info = {}
    info['mc'] = get_ocp_chrony_mc(k8s_handler)
    info['config'] = get_ocp_chrony_config(linux_handlers)
    info['state'] = get_ocp_chrony_state(linux_handlers)

    return info
