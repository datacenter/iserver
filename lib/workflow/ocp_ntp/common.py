from lib.workflow import ocp_common
from lib.workflow.ocp_access import check as ocp_check


def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow'
    return params


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
