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


@click.command("racks")
@click.pass_obj
@click.option("--manager", "ucsm", default='', callback=validations.validate_ucsm_name, help="UCSM manager name")
@click.option("--power", is_flag=True, show_default=True, default=False, help="Power state information")
@click.option("--thermal", is_flag=True, show_default=True, default=False, help="Thermal state information")
@click.option("--env", is_flag=True, show_default=True, default=False, help="Environmental state information")
@click.option("--net", is_flag=True, show_default=True, default=False, help="Networking state information")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ucsm_racks_command(
        ctx,
        ucsm,
        power,
        thermal,
        env,
        net,
        output,
        devel
        ):
    """Get ucsm racks"""

    # iserver get ucsm racks

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

        if env:
            power = True
            thermal = True

        racks_info = ucsm_handler.get_racks(
            power=power,
            thermal=thermal,
            net=net
        )
        if racks_info is None:
            ctx.my_output.error('Failed to get racks info')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    racks_info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(racks_info)

        ucsm_handler.print_racks(
            racks_info,
            power=power,
            thermal=thermal
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
