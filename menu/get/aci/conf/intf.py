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


@click.command("intf")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--view", "-v", type=click.Choice(['state'], case_sensitive=False), multiple=False, default='state', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--ttl", "requested_ttl", default=-1, show_default=True, help="Cache ttl")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_configuration_interface_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        view,
        output,
        requested_ttl,
        devel
        ):
    """Get aci configuration interface"""

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
            requested_ttl=requested_ttl
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        configurations = apic_handler.get_configuration_interfaces()

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    configurations,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(configurations)

        if 'state' in view:
            aci_output_handler.print_configuration_interface(
                configurations,
                title=True
            )

        if configurations is None or len(configurations) == 0:
            raise NoResultExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
