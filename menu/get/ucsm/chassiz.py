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


@click.command("chassiz")
@click.pass_obj
@click.option("--manager", "ucsm", default='', callback=validations.validate_ucsm_name, help="UCSM manager name")
@click.option("--blade", is_flag=True, show_default=True, default=False, help="Blade information")
@click.option("--power", is_flag=True, show_default=True, default=False, help="Power state information")
@click.option("--thermal", is_flag=True, show_default=True, default=False, help="Thermal state information")
@click.option("--env", is_flag=True, show_default=True, default=False, help="Environmental state information")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ucsm_chassiz_command(
        ctx,
        ucsm,
        blade,
        power,
        thermal,
        env,
        output,
        devel
        ):
    """Get ucsm chassiz"""

    # iserver get ucsm chassiz

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

        chassiz_info = ucsm_handler.get_chassiz(
            blade=blade,
            power=power,
            thermal=thermal
        )
        if chassiz_info is None:
            ctx.my_output.error('Chassis info get failed')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    chassiz_info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(chassiz_info)

        ucsm_handler.print_chassiz(
            chassiz_info,
            blade=blade,
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
