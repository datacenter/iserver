import sys
import traceback
import click

from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ws")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--mo", "managed_objects", default=[], multiple=True, help="Managed objects")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def set_aci_ws_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        managed_objects,
        debug
        ):
    """Set aci websocket"""

    # iserver set aci ws

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        if len(managed_objects) == 0:
            ctx.my_output.error(
                'Define at least one managed object'
            )
            ctx.my_output.default('Example:')
            ctx.my_output.default('- /api/class/fvTenant')
            ctx.my_output.default('- /api/node/class/faultInst')
            ctx.my_output.default('- /api/node/class/faultDelegate')
            raise ErrorExit

        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            debug=debug
        )
        if apic_handler is None:
            raise ErrorExit

        apic_handler.ws_run(
            managed_objects
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except KeyboardInterrupt:
        ctx.busy = False
        sys.exit(0)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
