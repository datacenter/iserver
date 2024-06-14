import sys
import json
import threading
import traceback
import click

from lib.intersight import compute
from lib.intersight import compute_output
from lib import context

from menu import defaults
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--node", "node_names", multiple=True, default=['any'], help="Node name patterns")
@click.option("--address", "server_ip", callback=validations.validate_ips, multiple=True, help="Server IP")
@click.option("--view", "-v", default=['state'], help="['state']", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_server_command(
        ctx,
        iaccount,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        node_names,
        server_ip,
        view,
        output,
        no_cache,
        devel
        ):
    """Get server connectivity information"""

    # iserver get aci server

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state',
        'state',
        []
    )

    try:
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
            'any',
            pod_id=''
        )
        if nodes_info is None:
            raise ErrorExit

        if output != 'json':
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)
        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
        match_rules = compute_handler.get_mo_match_rules(
            ip_filter=server_ip
        )
        servers_mo = compute_handler.get_mo(
            match_rules=match_rules,
            include_rack=True,
            include_blade=True
        )
        if len(servers_mo) == 0:
            ctx.busy = False
            ctx.my_output.error('No server found')
            raise ErrorExit

        settings = {}
        settings['net'] = True

        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            None,
            0
        )

        servers_connectivity_info = []
        for server_info in servers_info:
            servers_connectivity_info.append(
                apic_handler.get_server_connectivity(
                    server_info,
                    nodes_info
                )
            )

        context_handler = context.Context(log_id=ctx.run_id)
        context_handler.set(
            'phy',
            apic_handler.get_context_server_connectivity_interface(servers_connectivity_info)
        )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    servers_connectivity_info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(servers_connectivity_info)

        for server_connectivity_info in servers_connectivity_info:
            compute_output_handler.print_summary_table(
                [server_connectivity_info],
                title=True
            )
            compute_output_handler.print_aci(
                server_connectivity_info,
                title=True
            )

        ctx.my_output.default('Ctx: phy', before_newline=True)

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
