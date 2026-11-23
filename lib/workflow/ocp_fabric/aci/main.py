import time
from lib.workflow.ocp_fabric import common
from lib.workflow.ocp_fabric.aci import check
from lib.workflow.ocp_fabric.aci import delete
from lib.workflow.ocp_fabric.aci import patch


def verify_server(handler, server, my_output):
    for item in server:
        for interface in item['interface']:
            node_info = handler.get_node(
                node_id=interface['node'],
                cache_enabled=False
            )
            if node_info is None:
                my_output.error('Node not found: %s' % (interface['node']))
                return None

            interface['pod'] = node_info['podId']

    return server


def verify_bgp(handler, fabric, my_output):
    if fabric['check_mode'] == 'full':
        if fabric['bgp']['enabled']:
            for key in ['leaf_A', 'leaf_B']:
                node_info = handler.get_node(
                    node_id=fabric['bgp'][key]['id'],
                    cache_enabled=False
                )
                if node_info is None:
                    my_output.error('Node not found: %s' % (fabric['bgp'][key]['id']))
                    return None

                fabric['bgp'][key]['pod'] = node_info['podId']

    return fabric


def run(mode, fabric, server, my_output, log_id):
    handler = common.get_handler('aci', fabric['apic'], my_output, log_id)
    if handler is None:
        my_output.error('APIC communication failed: %s' % (fabric['apic']))
        return False

    server = verify_server(handler, server, my_output)
    if server is None:
        return False

    fabric = verify_bgp(handler, fabric, my_output)
    if fabric is None:
        return False

    if mode == 'check':
        success = check.run(fabric, server, my_output, log_id)
        if not success:
            return False

    if mode == 'patch':
        success = patch.run(fabric, server, my_output, log_id)
        if not success:
            return False

        my_output.default('Wait before checking...', before_newline=True, after_newline=True)
        time.sleep(10)

        success = check.run(fabric, server, my_output, log_id, show_input=False)
        if not success:
            return False

    if mode == 'delete':
        success = delete.run(fabric, server, my_output, log_id)
        if not success:
            return False

    return True
