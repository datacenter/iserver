import sys
import traceback
import click

from menu import common

from lib.aci import apic
from lib.aci import settings
from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("controller")
@click.pass_obj
@click.option("--name", "apic_name", default='', help="APIC name")
@click.option("--ip", "apic_ip", default='', help="APIC IP/FQDN")
@click.option("--port", "apic_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "apic_username", default='', help="APIC username")
@click.option("--password", "apic_password", default='', help="APIC password")
@click.option("--domain", "apic_domain", default='', help="Administrative domain")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify authenticaition")
def set_aci_controller_command(
        ctx,
        apic_name,
        apic_ip,
        apic_port,
        apic_username,
        apic_password,
        apic_domain,
        verify
        ):
    """Set aci controller access details"""

    # iserver set aci controller

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(apic_name) == 0:
            ctx.my_output.error('Define apic entry name')
            raise ErrorExit

        if len(apic_ip) == 0:
            ctx.my_output.error('Define apic ip address')
            raise ErrorExit

        if len(apic_username) == 0:
            ctx.my_output.error('Define apic username')
            raise ErrorExit

        if len(apic_password) == 0:
            ctx.my_output.error('Define apic password')
            raise ErrorExit

        if verify:
            apic_handler = apic.Apic(
                apic_ip,
                apic_port,
                apic_username,
                apic_password,
                log_id=ctx.run_id
            )
            if not apic_handler.is_connected():
                ctx.my_output.error('Failed to connect to APIC')
                raise ErrorExit

            ctx.my_output.default('APIC authentication successful')

        settings_handler = settings.ApicSettings(log_id=ctx.run_id)
        success = settings_handler.set_apic_controller(
            apic_name,
            apic_ip,
            apic_port,
            apic_username,
            apic_password,
            domain=apic_domain
        )
        if not success:
            ctx.my_output.error('Failed to define apic entry')
            raise ErrorExit

        controller = settings_handler.get_apic_controller(apic_name)

        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        aci_output_handler.print_apic_controllers(
            [controller],
            show_password=False
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
