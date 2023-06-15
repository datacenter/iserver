import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("hsrp")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_names", multiple=True, help="Node name patterns")
@click.option("--role", "node_role", type=click.Choice(['any', 'leaf', 'spine'], case_sensitive=False), default='any', show_default=True)
@click.option("--vrf", "hsrp_vrf", default='', callback=validations.empty_string_to_none, help="Filter by VRF name")
@click.option("--id", "hsrp_neighbor", default='', callback=validations.empty_string_to_none, help="Filter by neighbor")
@click.option("--view", "-v", type=click.Choice(['default', 'vrf', 'intf'], case_sensitive=False), multiple=True, show_default=False)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_proto_hsrp_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_names,
        node_role,
        hsrp_vrf,
        hsrp_neighbor,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci node protocol hsrp"""

    # iserver get aci node proto hsrp

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            show_selected=False,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        nodes_info = validations.validate_apic_node_names(
            ctx,
            apic_handler,
            node_names,
            node_role,
            pod_id=pod_id,
        )
        if nodes_info is None:
            raise ErrorExit

        hsrp_filter = []
        if hsrp_neighbor is not None:
            hsrp_filter.append(
                'id:%s' % (hsrp_neighbor)
            )

        if hsrp_vrf is not None:
            hsrp_filter.append(
                'vrf:%s' % (hsrp_vrf)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        instances = []
        interfaces = []
        domains = []

        for node_info in nodes_info:
            proto_info = apic_handler.get_protocol_hsrp(
                node_info['podId'],
                node_info['id'],
                hsrp_filter=hsrp_filter
            )

            if proto_info is None:
                continue

            instances.append(
                proto_info
            )
            interfaces = interfaces + proto_info['interfaces']
            domains = domains + proto_info['domains']

        ctx.busy = False

        if len(instances) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    instances,
                    indent=4
                )
            )
            return

        if 'default' in view:
            ctx.my_output.json_output(instances)
            aci_output_handler.print_proto_hsrp_instances(
                instances
            )

        if 'vrf' in view:
            ctx.my_output.json_output(domains)
            aci_output_handler.print_proto_hsrp_domains(
                domains
            )

        if 'intf' in view:
            ctx.my_output.json_output(interfaces)
            aci_output_handler.print_proto_hsrp_interfaces(
                interfaces
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
