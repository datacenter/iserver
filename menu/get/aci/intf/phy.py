import sys
import copy
import json
import threading
import traceback
import click

from lib.aci import output as aci_output
from lib import context

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("phy")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--id", "interface_ids", multiple=True, default=[], help="Filter by interface id")
@click.option("--switching", type=click.Choice(['any', 'enabled', 'disabled'], case_sensitive=False), default='any', show_default=True, help="Filter by switching state")
@click.option("--oper", type=click.Choice(['any', 'up', 'down'], case_sensitive=False), default='any', show_default=True, help="Filter by operational state")
@click.option("--type", "interface_type", type=click.Choice(['any', 'leaf', 'fab'], case_sensitive=False), default='any', show_default=True, help="Filter by port type")
@click.option("--qos", type=click.Choice(['any', 'data', 'data-rx', 'data-tx', 'drops', 'drops-rx', 'drops-tx'], case_sensitive=False), default='any', show_default=True, help="Filter by qos counters")
@click.option("--layer", type=click.Choice(['any', 'l2', 'l3'], case_sensitive=False), default='any', show_default=True, help="Filter by layer")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by mac address")
@click.option("--speed", type=click.Choice(['any', '1G', '10G', '25G', '40G', '100G', '400G'], case_sensitive=False), default='any', show_default=True, help="Filter by interface speed")
@click.option("--fec", default='', callback=validations.empty_string_to_none, show_default=True, help="Filter by fec")
@click.option("--optics", default='', callback=validations.empty_string_to_none, help="Filter by transceiver optics")
@click.option("--trans", default='', callback=validations.empty_string_to_none, help="Filter by transceiver type")
@click.option("--epg", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--vlan", default='', callback=validations.empty_string_to_none, help="Filter by vlan value")
@click.option("--evlan", default='', callback=validations.empty_string_to_none, help="Filter by encapsulation vlan value")
@click.option("--fvxlan", default='', callback=validations.empty_string_to_none, help="Filter by fabric vxlan value")
@click.option("--nei", default='', callback=validations.empty_string_to_none, help="Filter by cdp/lldp neight system name")
@click.option("--ctx", "user_context", default='', help="Filter by context")
@click.option("--set-ctx", "set_context", is_flag=True, show_default=True, default=False, help="Set phy context")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|l2|trans|vlan|epg|load|eee|nei|cdp|lldp|pg|pol|aaep|ether|err|qos|fault|hfault|event|audit|diag|all|verbose]", show_default=True, multiple=True)
@click.option("--pivot", is_flag=True, show_default=True, default=False, help="Pivot view")
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_phy_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        interface_ids,
        switching,
        oper,
        interface_type,
        qos,
        layer,
        mac,
        speed,
        fec,
        trans,
        optics,
        epg,
        vlan,
        evlan,
        fvxlan,
        nei,
        user_context,
        set_context,
        fault,
        fault_severity,
        fault_when,
        view,
        pivot,
        output,
        no_cache,
        devel
        ):
    """Get aci node physical interface"""

    # iserver get aci node intf phy

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|l2|trans|vlan|epg|load|eee|nei|cdp|lldp|pg|pol|aaep|ether|err|qos|fault|hfault|event|audit|diag|all|verbose',
        'state',
        [
            'diag:fault,hfault,event,audit'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        context_handler = context.Context(log_id=ctx.run_id)

        if len(user_context) == 0:
            apic_handlers = validations.validate_apic_controllers_with_nodes(
                ctx,
                controller,
                controller_ip,
                controller_port,
                controller_username,
                controller_password,
                node_names,
                node_role,
                pod_id=pod_id,
                no_cache=no_cache
            )
            if apic_handlers is None:
                raise ErrorExit

        if len(user_context) > 0:
            context_interfaces = context_handler.get(
                user_context
            )
            if context_interfaces is None:
                ctx.my_output.error('Unknown context: %s' % (user_context))
                raise ErrorExit

            if len(context_interfaces) == 0:
                ctx.my_output.error('Empty context: %s' % (user_context))
                raise ErrorExit

            apic_handlers = validations.validate_apic_controllers_with_context_interfaces(
                ctx,
                context_interfaces
            )
            if apic_handlers is None:
                raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        if 'audit' in view:
            audit_info = True

        interfaces = []
        fault_record = []
        fault_inst = []
        event = []

        ether_stats_info = False
        fc_stats_info = False
        epg_stats_info = False
        load_info = False
        eee_info = False
        cdp_info = False
        lldp_info = False
        policy_info = False
        qos_info = False
        cap_info = False
        pc_info = False

        if 'trans' in view:
            fc_stats_info = True

        if 'load' in view:
            load_info = True

        if 'qos' in view or 'live' in view:
            qos_info = True

        if 'ether' in view or 'err' in view:
            ether_stats_info = True

        if 'eee' in view:
            eee_info = True

        if 'epg' in view or 'vlan' in view:
            epg_stats_info = True

        if 'nei' in view:
            cdp_info = True
            lldp_info = True

        if 'cdp' in view:
            cdp_info = True

        if 'lldp' in view:
            lldp_info = True

        if 'pol' in view or 'pg' in view or 'aaep' in view:
            policy_info = True

        if 'verbose' in view:
            cap_info = True
            pc_info = True

        interface_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

        if len(interface_ids) > 0:
            ids = []
            for interface_id in interface_ids:
                if len(interface_id.split('-')) == 2:
                    (start_id, end_id) = interface_id.split('-')
                    if len(start_id.split('/')) != len(end_id.split('/')):
                        ctx.my_output.error(
                            'Unsupported port range'
                        )
                        raise ErrorExit

                    if len(start_id.split('/')) not in [2, 3]:
                        ctx.my_output.error(
                            'Unsupported port range'
                        )
                        raise ErrorExit

                    if '*' in start_id.split('/') or '*' in end_id.split('/'):
                        ctx.my_output.error(
                            'Unsupported port range'
                        )
                        raise ErrorExit

                    module_id = '/'.join(start_id.split('/')[:-1])
                    start_port_id = start_id.split('/')[-1]
                    end_port_id = end_id.split('/')[-1]

                    if int(start_port_id) > int(end_port_id):
                        ctx.my_output.error(
                            'Unsupported port range'
                        )
                        raise ErrorExit

                    port_id = int(start_port_id)
                    while True:
                        range_id = '%s/%s' % (
                            module_id,
                            port_id
                        )
                        if range_id.startswith('eth'):
                            ids.append(
                                range_id
                            )
                        else:
                            ids.append(
                                'eth%s' % (range_id)
                            )

                        port_id = port_id + 1
                        if port_id > int(end_port_id):
                            break

                if len(interface_id.split('-')) == 1:
                    if interface_id.startswith('eth'):
                        ids.append(
                            interface_id
                        )
                    else:
                        ids.append(
                            'eth%s' % (interface_id)
                        )

                interface_filter.append(
                    'ids:%s' % (','.join(ids))
                )

        if switching != 'any':
            interface_filter.append(
                'switching:%s' % (switching)
            )

        if oper != 'any':
            interface_filter.append(
                'oper:%s' % (oper)
            )

        if interface_type != 'any':
            interface_filter.append(
                'type:%s' % (interface_type)
            )

        if layer != 'any':
            if layer == 'l2':
                interface_filter.append(
                    'layer:switched'
                )
            if layer == 'l3':
                interface_filter.append(
                    'layer:routed'
                )

        if mac is not None:
            interface_filter.append(
                'mac:%s' % (mac)
            )

        if speed != 'any':
            interface_filter.append(
                'speed:%s' % (speed)
            )

        if fec is not None:
            interface_filter.append(
                'fec:%s' % (fec)
            )

        if trans is not None:
            fc_stats_info = True
            interface_filter.append(
                'trans:%s' % (trans)
            )

        if optics is not None:
            fc_stats_info = True
            interface_filter.append(
                'optics:%s' % (optics)
            )

        if epg is not None:
            epg_stats_info = True
            interface_filter.append(
                'epg:%s' % (epg)
            )

        if vlan is not None:
            epg_stats_info = True
            interface_filter.append(
                'vlan:%s' % (vlan)
            )

        if evlan is not None:
            epg_stats_info = True
            interface_filter.append(
                'evlan:%s' % (evlan)
            )

        if fvxlan is not None:
            epg_stats_info = True
            interface_filter.append(
                'fvxlan:%s' % (fvxlan)
            )

        if nei is not None:
            cdp_info = True
            lldp_info = True
            interface_filter.append(
                'nei:%s' % (nei)
            )

        if qos != 'any':
            qos_info = True
            interface_filter.append(
                'qos:%s' % (qos)
            )

        if fault:
            interface_filter.append(
                'fault:any'
            )

        if fault_severity != 'any':
            hfault_filter.append(
                'severity:%s' % (fault_severity)
            )

        if fault_when is not None:
            hfault_filter.append(
                'timestamp:%s' % (fault_when)
            )
            event_filter.append(
                'timestamp:%s' % (fault_when)
            )
            audit_filter.append(
                'timestamp:%s' % (fault_when)
            )

        if 'live' in view:
            qos_references = {}
            for apic_handler in apic_handlers:
                for node_info in apic_handler['nodes']:
                    key = '%s.%s' % (
                        node_info['podId'],
                        node_info['id']
                    )
                    qos_references[key] = None

            previous_output = None
            initial = True
            while True:
                interfaces = []
                for apic_handler in apic_handlers:
                    for node_info in apic_handler['nodes']:
                        key = '%s.%s' % (
                            node_info['podId'],
                            node_info['id']
                        )
                        node_interfaces = apic_handler['handler'].get_interfaces_phy(
                            node_info['podId'],
                            node_info['id'],
                            interface_filter=interface_filter,
                            qos_info=qos_info,
                            qos_references=qos_references[key]
                        )

                        interfaces = interfaces + node_interfaces
                        if initial:
                            qos_references[key] = copy.deepcopy(node_interfaces)

                if initial:
                    initial = False
                    continue

                aci_output_handler.my_output.clear_output()
                aci_output_handler.print_interfaces_phy_qos(
                    interfaces,
                    stream='output'
                )
                printed_output = aci_output_handler.my_output.get_output()

                if previous_output is not None:
                    for counter in range(0, len(previous_output.split('\n')) + 1):
                        print('\033[1A', end='\x1b[2K')

                print(printed_output)
                previous_output = printed_output

                user_input = ctx.my_output.get_input('Press enter to exit...', timeout=2)
                if user_input is not None:
                    break

            return

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        interfaces = []
        fault_record = []
        fault_inst = []
        event = []
        audit = []
        context_phy = []

        for apic_handler in apic_handlers:
            for node_info in apic_handler['nodes']:
                if len(user_context) == 0:
                    aif = copy.deepcopy(interface_filter)
                else:
                    node_context_interfaces = []
                    for context_interface in context_interfaces:
                        #aci:apic21:pod-1:node-2208:eth1/2/3
                        if apic_handler['name'] == context_interface.split(':')[1]:
                            if context_interface.split(':')[2].split('-')[1] == node_info['podId']:
                                if context_interface.split(':')[3].split('-')[1] == node_info['id']:
                                    node_context_interfaces.append(
                                        context_interface.split(':')[4]
                                    )

                    aif = []
                    aif.append(
                        'ids:%s' % (','.join(node_context_interfaces))
                    )

                node_interfaces = apic_handler['handler'].get_interfaces_phy(
                    node_info['podId'],
                    node_info['id'],
                    interface_filter=aif,
                    fc_stats_info=fc_stats_info,
                    epg_stats_info=epg_stats_info,
                    load_info=load_info,
                    eee_info=eee_info,
                    cdp_info=cdp_info,
                    lldp_info=lldp_info,
                    policy_info=policy_info,
                    qos_info=qos_info,
                    ether_stats_info=ether_stats_info,
                    cap_info=cap_info,
                    pc_info=pc_info,
                    fault_info=fault_info,
                    hfault_info=hfault_info,
                    hfault_filter=hfault_filter,
                    event_info=event_info,
                    event_filter=event_filter,
                    audit_info=audit_info,
                    audit_filter=audit_filter
                )

                if node_interfaces is None:
                    continue

                interfaces = interfaces + node_interfaces

                for interface in node_interfaces:
                    if 'eventLog' in interface:
                        if interface['eventLog'] is not None:
                            event = event + interface['eventLog']

                    if 'faultRecord' in interface:
                        if interface['faultRecord'] is not None:
                            fault_record = fault_record + interface['faultRecord']

                    if 'faultInst' in interface:
                        if interface['faultInst'] is not None:
                            fault_inst = fault_inst + interface['faultInst']

                    if 'auditLog' in interface:
                        if interface['auditLog'] is not None:
                            audit = audit + interface['auditLog']

                    interface_name = 'apic:%s:pod-%s:node-%s:%s' % (
                        interface['apic'],
                        interface['podId'],
                        interface['nodeId'],
                        interface['id']
                    )
                    if interface_name not in context_phy:
                        context_phy.append(
                            interface_name
                        )

        event = sorted(
            event,
            key=lambda i: i['timestamp']
        )

        fault_record = sorted(
            fault_record,
            key=lambda i: i['timestamp']
        )

        fault_inst = sorted(
            fault_inst,
            key=lambda i: i['timestamp']
        )

        audit = sorted(
            audit,
            key=lambda i: i['timestamp']
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    interfaces,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(interfaces)

        if 'state' in view:
            aci_output_handler.print_interfaces_phy_state(
                interfaces,
                title=True
            )

        if 'l2' in view:
            aci_output_handler.print_interfaces_phy_l2(
                interfaces,
                title=True
            )

        if 'trans' in view:
            aci_output_handler.print_interfaces_phy_trans(
                interfaces,
                title=True
            )

        if 'epg' in view:
            aci_output_handler.print_interfaces_phy_epg(
                interfaces,
                title=True
            )

        if 'vlan' in view:
            if pivot:
                aci_output_handler.print_interfaces_phy_vlan_pivot(
                    interfaces,
                    title=True
                )

            if not pivot:
                aci_output_handler.print_interfaces_phy_vlan(
                    interfaces,
                    title=True
                )

        if 'load' in view:
            aci_output_handler.print_interfaces_phy_load(
                interfaces,
                title=True
            )

        if 'eee' in view:
            aci_output_handler.print_interfaces_phy_eee(
                interfaces,
                title=True
            )

        if 'nei' in view:
            aci_output_handler.print_interfaces_phy_nei(
                interfaces,
                title=True
            )

        if 'cdp' in view:
            aci_output_handler.print_interfaces_phy_cdp(
                interfaces,
                title=True
            )

        if 'lldp' in view:
            aci_output_handler.print_interfaces_phy_lldp(
                interfaces,
                title=True
            )

        if 'pol' in view:
            aci_output_handler.print_interfaces_phy_policy(
                interfaces,
                title=True
            )

        if 'pg' in view:
            aci_output_handler.print_interfaces_phy_policy_group(
                interfaces,
                title=True
            )

        if 'aaep' in view:
            aci_output_handler.print_interfaces_phy_aaep(
                interfaces,
                title=True
            )

        if 'qos' in view:
            aci_output_handler.print_interfaces_phy_qos(
                interfaces,
                title=True
            )

        if 'ether' in view:
            aci_output_handler.print_interfaces_phy_ether(
                interfaces,
                title=True
            )

        if 'err' in view:
            aci_output_handler.print_interfaces_phy_err(
                interfaces,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_interface_phy_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_interface_phy_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_interface_phy_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_interface_phy_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if 'verbose' in view:
            for interface in interfaces:
                aci_output_handler.print_interface_phy(
                    interface
                )

        if set_context:
            if not context_handler.set('phy', context_phy):
                ctx.my_output.error('Failed to set interface context')

        if len(interfaces) == 0:
            raise NoResultExit

        ctx.my_output.default('Filter: id, switching, oper, type, qos, layer, mac, speed, fec, optics, trans', before_newline=True)
        ctx.my_output.default('        epg, vlan, evlan, fvxlan, nei, fault, severity, when')
        ctx.my_output.default('View:   state (def), l2, trans, vlan, epg, load, eee, nei, cdp, lldp')
        ctx.my_output.default('        pg, pol, aaep, ether, err, qos, fault, hfault, event, audit, diag, all, verbose')

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
