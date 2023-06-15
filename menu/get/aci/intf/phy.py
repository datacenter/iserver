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
@click.option("--ctx", "user_context", default='', callback=validations.validate_context, help="Filter by context")
@click.option("--view", "-v", type=click.Choice(['default', 'trans', 'vlan', 'epg', 'load', 'eee', 'nei', 'cdp', 'lldp', 'pg', 'pol', 'aaep', 'ether', 'err', 'qos', 'live', 'verbose'], case_sensitive=False), multiple=True)
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
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node physical interface"""

    # iserver get aci node intf phy

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
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
            user_context=user_context,
            no_cache=no_cache
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

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

        if 'verbose' in view or 'trans' in view:
            fc_stats_info = True

        if 'verbose' in view or 'load' in view:
            load_info = True

        if 'verbose' in view or 'qos' in view or 'live' in view:
            qos_info = True

        if 'verbose' in view or 'ether' in view or 'err' in view:
            ether_stats_info = True

        if 'verbose' in view or 'eee' in view:
            eee_info = True

        if 'verbose' in view or 'epg' in view or 'vlan' in view:
            epg_stats_info = True

        if 'verbose' in view or 'nei' in view:
            cdp_info = True
            lldp_info = True

        if 'verbose' in view or 'cdp' in view:
            cdp_info = True

        if 'verbose' in view or 'lldp' in view:
            lldp_info = True

        if 'verbose' in view or 'pol' in view or 'pg' in view or 'aaep' in view:
            policy_info = True

        if 'verbose' in view:
            cap_info = True
            pc_info = True

        interface_filter = []

        if len(interface_ids) > 0:
            ids = []
            for interface_id in interface_ids:
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

        phy_context = {}
        phy_context['apic'] = []
        phy_context['node'] = {}
        phy_context['interface'] = {}

        for apic_handler in apic_handlers:
            apic_interface_filter = copy.deepcopy(interface_filter)
            if user_context is not None:
                apic_interface_filter.append(
                    'ctx:%s' % (','.join(user_context['value']['interface'][apic_handler['name']]))
                )

            for node_info in apic_handler['nodes']:
                node_interfaces = apic_handler['handler'].get_interfaces_phy(
                    node_info['podId'],
                    node_info['id'],
                    interface_filter=apic_interface_filter,
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
                    pc_info=pc_info
                )

                if node_interfaces is None:
                    continue

                interfaces = interfaces + node_interfaces

                if len(node_interfaces) > 0:
                    if apic_handler['name'] not in phy_context['apic']:
                        phy_context['apic'].append(
                            apic_handler['name']
                        )
                        phy_context['node'][apic_handler['name']] = []
                        phy_context['interface'][apic_handler['name']] = []

                    node_name = apic_handler['handler'].get_node_name(node_info['id'])
                    if node_name not in phy_context['node'][apic_handler['name']]:
                        phy_context['node'][apic_handler['name']].append(node_name)

                    for node_interface in node_interfaces:
                        interface_name = 'pod-%s:node-%s:%s' % (
                            node_interface['podId'],
                            node_interface['nodeId'],
                            node_interface['id']
                        )
                        if interface_name not in phy_context['interface'][apic_handler['name']]:
                            phy_context['interface'][apic_handler['name']].append(interface_name)

        ctx.busy = False

        if len(interfaces) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    interfaces,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(interfaces)

        if 'default' in view:
            aci_output_handler.print_interfaces_phy_state(
                interfaces
            )

        if 'trans' in view:
            aci_output_handler.print_interfaces_phy_trans(
                interfaces
            )

        if 'epg' in view:
            aci_output_handler.print_interfaces_phy_epg(
                interfaces
            )

        if 'vlan' in view:
            aci_output_handler.print_interfaces_phy_vlan(
                interfaces
            )

        if 'load' in view:
            aci_output_handler.print_interfaces_phy_load(
                interfaces
            )

        if 'eee' in view:
            aci_output_handler.print_interfaces_phy_eee(
                interfaces
            )

        if 'nei' in view:
            aci_output_handler.print_interfaces_phy_nei(
                interfaces
            )

        if 'cdp' in view:
            aci_output_handler.print_interfaces_phy_cdp(
                interfaces
            )

        if 'lldp' in view:
            aci_output_handler.print_interfaces_phy_lldp(
                interfaces
            )

        if 'pol' in view:
            aci_output_handler.print_interfaces_phy_policy(
                interfaces
            )

        if 'pg' in view:
            aci_output_handler.print_interfaces_phy_policy_group(
                interfaces
            )

        if 'aaep' in view:
            aci_output_handler.print_interfaces_phy_aaep(
                interfaces
            )

        if 'qos' in view:
            aci_output_handler.print_interfaces_phy_qos(
                interfaces
            )

        if 'ether' in view:
            aci_output_handler.print_interfaces_phy_ether(
                interfaces
            )

        if 'err' in view:
            aci_output_handler.print_interfaces_phy_err(
                interfaces
            )

        if 'verbose' in view:
            for interface in interfaces:
                aci_output_handler.print_interface_phy(
                    interface
                )

        context_handler = context.Context(log_id=ctx.run_id)
        success = context_handler.set(
            'phy',
            phy_context
        )
        if not success:
            ctx.my_output.error('Failed to set interface context')
        else:
            ctx.my_output.default('Interface context: phy')

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
