from lib.workflow.ocp_fabric import common
from lib.aci import output as aci_output


def print_state(fabric, my_output, log_id):
    aci_output_handler = aci_output.ApicOutput(log_id=log_id)
    for controller in fabric['controller']:
        if controller['type'] != 'aci':
            continue

        if 'bgp' not in controller:
            continue

        aci_handler = common.get_handler(controller['apic'], my_output, log_id)
        if aci_handler is None:
            my_output.error('Failed to get ACI handler: %s' % (controller['apic']))
            return False

        for key in ['leaf_A', 'leaf_B']:
            node_info = aci_handler.get_node(
                node_id=controller['bgp'][key]['id'],
                cache_enabled=False
            )
            if node_info is None:
                my_output.error('ACI node not found: %s' % (controller['bgp'][key]['id']))
                return False

            proto_info = aci_handler.get_protocol_bgp(
                node_info['podId'],
                controller['bgp'][key]['id'],
                bgp_filter=['asn:%s' % (controller['bgp']['asn'])],
                instance_info=True,
                neighbor_info=True,
                domain_info=True,
                stats_info=True
            )
            if proto_info is None:
                return False
            
            my_output.default(
                'ACI [%s] - BGP Neighbor on node [%s]' % (controller['apic'], controller['bgp'][key]['id']),
                before_newline=True,
                underline=True
            )
            aci_output_handler.print_proto_bgp_neighbors(
                proto_info['neighbor'],
                title=False
            )
