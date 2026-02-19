import copy
from lib.workflow.ocp_fabric.aci import common as aci_common


def get_handler(controller_type, controller_name, my_output, log_id):
    if controller_type == 'aci':
        return aci_common.get_handler(controller_name, my_output, log_id)
    return None


def get_controller_ip(controller, my_output, log_id):
    if controller['type'] == 'aci':
        return aci_common.get_controller_ip(controller['apic'], my_output, log_id)
    return None


def get_domain_servers(domain_name, servers):
    domain_servers = []
    for server in servers:
        domain_interfaces = []
        for interface in server['interface']:
            if interface['domain'] == domain_name:
                domain_interfaces.append(
                    interface
                )

        if len(domain_interfaces) > 0:
            server['interface'] = copy.deepcopy(domain_interfaces)
            domain_servers.append(
                server
            )

    return domain_servers
