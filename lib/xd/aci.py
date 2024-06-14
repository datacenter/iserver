from lib.aci import settings as aci_settings
from lib.aci import apic


def get_aci_handler(controller_name, log_id=None):
    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    aci_controllers = aci_settings_handler.get_apic_controllers()
    if aci_controllers is not None:
        for aci_controller in aci_controllers:
            if aci_controller['name'] == controller_name:
                apic_handler = apic.Apic(
                    aci_controller['ip'],
                    aci_controller['port'],
                    aci_controller['username'],
                    aci_controller['password'],
                    apic_name=aci_controller['name'],
                    log_id=log_id
                )
                return apic_handler

    return None


def get_any_aci_handler(log_id=None):
    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    aci_controllers = aci_settings_handler.get_apic_controllers()
    if aci_controllers is not None:
        for aci_controller in aci_controllers:
            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=log_id
            )
            return apic_handler

    return None


def get_aci_endpoints(log_id=None, fabric_info=True, macs=None, apic_ips=None):
    endpoints = []

    endpoint_filter = None
    if macs is not None:
        endpoint_filter = []
        for mac in macs:
            endpoint_filter.append('mac:%s' % (mac))

    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    aci_controllers = aci_settings_handler.get_apic_controllers()
    if aci_controllers is not None:
        for aci_controller in aci_controllers:
            if apic_ips is None or aci_controller['ip'] in apic_ips:
                apic_handler = apic.Apic(
                    aci_controller['ip'],
                    aci_controller['port'],
                    aci_controller['username'],
                    aci_controller['password'],
                    apic_name=aci_controller['name'],
                    log_id=log_id
                )

                apic_endpoints = apic_handler.get_endpoints(
                    endpoint_filter=endpoint_filter,
                    fabric_info=fabric_info
                )
                if apic_endpoints is None:
                    continue

                for apic_endpoint in apic_endpoints:
                    apic_endpoint['apic'] = aci_controller['name']

                endpoints = endpoints + apic_endpoints

    return endpoints


def get_aci_cdp_info(log_id=None):
    aci_cdp_info = []

    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    aci_controllers = aci_settings_handler.get_apic_controllers()
    if aci_controllers is not None:
        for aci_controller in aci_controllers:
            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=log_id
            )

            nodes = apic_handler.get_nodes(
                node_filter=['role:leaf']
            )

            for node in nodes:
                node_cdp_info = apic_handler.get_protocol_cdp(
                    node['podId'],
                    node['id'],
                    include_instance=False,
                    include_interfaces=False
                )
                node_cdp_info['apic'] = aci_controller['name']
                aci_cdp_info.append(
                    node_cdp_info
                )

    return aci_cdp_info


def get_aci_lldp_info(log_id=None):
    aci_lldp_info = []

    aci_settings_handler = aci_settings.ApicSettings(log_id=log_id)
    aci_controllers = aci_settings_handler.get_apic_controllers()
    if aci_controllers is not None:
        for aci_controller in aci_controllers:
            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=log_id
            )

            nodes = apic_handler.get_nodes(
                node_filter=['role:leaf']
            )

            for node in nodes:
                node_lldp_info = apic_handler.get_protocol_lldp(
                    node['podId'],
                    node['id'],
                    instance_info=False,
                    stats_info=False,
                    adjacency_info=True
                )
                node_lldp_info['apic'] = aci_controller['name']
                aci_lldp_info.append(
                    node_lldp_info
                )

    return aci_lldp_info
