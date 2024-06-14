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


@click.command("summary")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--pod", "pod_id", default='', callback=validations.empty_string_to_none, help="Pod ID")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Node name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_node_intf_summary_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pod_id,
        node_name,
        output,
        no_cache,
        devel
        ):
    """Get aci node interface summary"""

    # iserver get aci node intf summary

    ctx.developer = devel
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        node_info = validations.validate_apic_node_name(
            ctx,
            apic_handler,
            node_name,
            pod_id=pod_id
        )
        if node_info is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        summary = apic_handler.get_interface_summary(
            pod_id=node_info['podId'],
            node_id=node_info['id']
        )

        ctx.busy = False

        if summary is None:
            ctx.my_output.error(
                'Failed to get interface summary'
            )
            raise ErrorExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    summary,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(summary)

        aci_output_handler.print_interface_summary(
            summary
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
