from lib.xd import aci as aci_helper
from lib.aci import output as aci_output


def print_ocp_vm_net_fabric_info(interfaces, log_id=None, stream='default'):
    if interfaces is None:
        return None

    endpoints = []
    for interface in interfaces:
        if 'endpoints' in interface:
            endpoints = endpoints + interface['endpoints']

    if len(endpoints) == 0:
        return None

    apic_handler = aci_helper.get_any_aci_handler(log_id=log_id)
    if apic_handler is None:
        return None

    aci_output_handler = aci_output.ApicOutput(log_id=log_id)
    aci_output_handler.my_output.clear_output()
    aci_output_handler.print_endpoints(
        endpoints,
        stream=stream,
        title=True
    )

    return apic_handler.my_output.get_output()
