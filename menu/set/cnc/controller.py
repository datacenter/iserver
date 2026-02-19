import sys
import traceback
import click

from menu import common

from lib.cnc import main as cnc
from lib.cnc import settings
from lib.cnc import output as cnc_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("controller")
@click.pass_obj
@click.option("--name", "cnc_name", default='', help="APIC name")
@click.option("--ip", "cnc_ip", default='', help="APIC IP/FQDN")
@click.option("--port", "cnc_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "cnc_username", default='', help="APIC username")
@click.option("--password", "cnc_password", default='', help="APIC password")
@click.option("--domain", "cnc_domain", default='', help="Administrative domain")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify authenticaition")
def set_cnc_controller_command(
        ctx,
        cnc_name,
        cnc_ip,
        cnc_port,
        cnc_username,
        cnc_password,
        cnc_domain,
        verify
        ):
    """Set cnc controller access details"""

    # iserver set cnc controller

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(cnc_name) == 0:
            ctx.my_output.error('Define cnc entry name')
            raise ErrorExit

        if len(cnc_ip) == 0:
            ctx.my_output.error('Define cnc ip address')
            raise ErrorExit

        if len(cnc_username) == 0:
            ctx.my_output.error('Define cnc username')
            raise ErrorExit

        if len(cnc_password) == 0:
            ctx.my_output.error('Define cnc password')
            raise ErrorExit

        if verify:
            cnc_handler = cnc.Cnc(
                cnc_ip,
                cnc_port,
                cnc_username,
                cnc_password,
                log_id=ctx.run_id
            )
            if not cnc_handler.is_connected():
                ctx.my_output.error('Failed to connect to CNC')
                raise ErrorExit

            ctx.my_output.default('CNC authentication successful')

        settings_handler = settings.CncSettings(log_id=ctx.run_id)
        success = settings_handler.set_cnc_controller(
            cnc_name,
            cnc_ip,
            cnc_port,
            cnc_username,
            cnc_password,
            domain=cnc_domain
        )
        if not success:
            ctx.my_output.error('Failed to define cnc entry')
            raise ErrorExit

        controller = settings_handler.get_cnc_controller(cnc_name)

        cnc_output_handler = cnc_output.CncOutput(log_id=ctx.run_id)
        cnc_output_handler.print_cnc_controllers(
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
