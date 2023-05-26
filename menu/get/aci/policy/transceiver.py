import sys
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("transceiver")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_policy_transceiver_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        output,
        verbose,
        devel
        ):
    """Get aci policy interface transceiver"""

    # iserver get aci policy interface transceiver

    ctx.developer = devel
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_username,
            controller_password
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if not verbose:
            policy = apic_handler.get_policy_interface_transceiver()
            ctx.busy = False
            aci_output_handler.print_policies_interface_transceiver(
                policy
            )
            ctx.my_output.json_output(policy)

        if verbose:
            policy = apic_handler.get_policy_interface_transceiver()
            ctx.busy = False

            for item in policy:
                aci_output_handler.print_policy_interface_transceiver(
                    item
                )

            ctx.my_output.json_output(policy)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
