import sys
import json
import traceback
import click

from lib.ucsm import manager

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("inventory")
@click.pass_obj
@click.option("--manager", "ucsm", default='', callback=validations.validate_ucsm_name, help="UCSM manager name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ucsm_inventory_command(
        ctx,
        ucsm,
        output,
        devel
        ):
    """Get ucsm inventory"""

    # iserver get ucsm inventory

    ctx.developer = devel

    try:
        ucsm_handler = manager.UcsManager(
            ucsm['ip'],
            ucsm['username'],
            ucsm['password'],
            log_id=ctx.run_id
        )

        if not ucsm_handler.is_connected():
            ctx.my_output.error('Failed to connect to UCSM')
            raise ErrorExit

        inventory = ucsm_handler.get_inventory()
        if inventory is None:
            ctx.my_output.error('Inventory info get failed')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    inventory,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(inventory)

        ucsm_handler.print_inventory(
            inventory
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
