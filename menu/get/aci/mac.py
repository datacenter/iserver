import sys
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


@click.command("mac")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--mac", "-m", multiple=True, help="MAC address")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_aci_mac_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        mac,
        output
        ):
    """Get aci mac address related objects"""

    ctx.developer = False
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=True
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()
        else:
            ctx.my_output.error(
                'Define single APIC'
            )
            raise ErrorExit

        apic_handler = apic_handlers[0]['handler']

        if len(mac) == 0:
            ctx.my_output.error(
                'Define MAC address'
            )
            raise ErrorExit

        endpoint_filter = []
        interface_filter = []
        adjacency_filter = []

        for mac_address in mac:
            if len(mac_address.split('ctx:')) == 2:
                context_handler = context.Context(log_id=ctx.run_id)
                new_mac = context_handler.get(
                   mac_address.split('ctx:')[1]
                )
                if output not in ['json']:
                    ctx.my_output.default('Ctx: %s' % (new_mac))
                if new_mac is None:
                    ctx.my_output.error('Unknown context: %s' % (mac_address.split('ctx:')[1]))
                    raise ErrorExit

            else:
                new_mac = [mac_address]

            for entry in new_mac:
                endpoint_filter.append(
                    'mac:%s' % (entry)
                )

                interface_filter.append(
                    'mac:%s' % (entry)
                )

                adjacency_filter.append(
                    'mac:%s' % (entry)
                )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        endpoints = []
        lacp = []
        lldp = []

        for apic_handler in apic_handlers:
            nodes_info = validations.validate_apic_node_names(
                ctx,
                apic_handler['handler'],
                ['any'],
                'any',
                pod_id='',
                silent=True
            )

            apic_endpoints = apic_handler['handler'].get_endpoints(
                endpoint_filter=endpoint_filter
            )
            for apic_endpoint in apic_endpoints:
                apic_endpoint['apic'] = apic_handler['name']

            endpoints = endpoints + apic_endpoints

            for node_info in nodes_info:
                proto_info = apic_handler['handler'].get_protocol_lacp(
                    node_info['podId'],
                    node_info['id'],
                    interface_info=True,
                    interface_filter=interface_filter
                )
                if proto_info is not None and proto_info['interfaces'] is not None:
                    lacp = lacp + proto_info['interfaces']

                proto_info = apic_handler['handler'].get_protocol_lldp(
                    node_info['podId'],
                    node_info['id'],
                    adjacency_filter=adjacency_filter,
                    instance_info=False,
                    stats_info=False,
                    adjacency_info=True,
                    fault_info=False,
                    hfault_info=False
                )
                if proto_info is not None and proto_info['adjacency'] is not None:
                    lldp = lldp + proto_info['adjacency']

        ctx.busy = False

        if len(endpoints) > 0:
            aci_output_handler.print_endpoints(
                endpoints,
                title=True
            )

        if len(lacp) > 0:
            aci_output_handler.print_proto_lacp_interfaces(
                lacp,
                title=True
            )

        if len(lldp) > 0:
            aci_output_handler.print_lldp_adjacency_endpoints(
                lldp,
                title=True
            )

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
