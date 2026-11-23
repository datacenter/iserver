from lib.workflow import ocp_common
from lib.workflow.ocp_access import check as ocp_check


def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow'
    return params


def get_ocp_container_policy_mc(handler):
    info = []

    machine_configs = handler.get_machine_configs(
        object_filter=['path:/etc/containers/policy.json']
    )
    for machine_config in machine_configs:
        if len(machine_config['file']) == 0:
            continue

        if machine_config['name'].startswith('rendered-'):
            continue

        if machine_config['name'].endswith('-generated-registries'):
            continue

        info.append(
            machine_config
        )

    return info


def get_ocp_container_policy_config(handlers):
    info = []

    for handler in handlers:
        item = {}
        item['name'] = handlers[handler].ocp_node_name
        item['ip'] = handlers[handler].management_ip

        container_policy_config = handlers[handler].get_container_policy_config_info()
        if container_policy_config is None:
            continue

        item['config'] = container_policy_config
        info.append(item)

    return info


def get_ocp_container_policy_info(k8s_handler, linux_handlers):
    info = {}
    info['mc'] = get_ocp_container_policy_mc(k8s_handler)
    info['config'] = get_ocp_container_policy_config(linux_handlers)
    return info
