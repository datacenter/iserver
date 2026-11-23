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
@click.option("--switch", "switch", default='', callback=validations.validate_nexus_name, help="Switch name")
@click.option("--ip", "switch_ip", default='', callback=validations.validate_ip, help="Switch IP")
@click.option("--username", "switch_username", default='', help="Switch Username")
@click.option("--password", "switch_password", default='', help="Switch Password")
@click.option("--mo", "managed_objects", default=[], multiple=True, help="Managed objects")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def set_nx_ws_command(
        ctx,
        switch,
        switch_ip,
        switch_username,
        switch_password,
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

        nexus_handler = validations.validate_nexus_switch(
            ctx,
            switch,
            switch_ip,
            switch_username,
            switch_password,
            debug=debug
        )
        if nexus_handler is None:
            raise ErrorExit

        nexus_handler.ws_run(
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
