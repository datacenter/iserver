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


@click.command("blades")
@click.pass_obj
@click.option("--manager", "ucsm", default='', callback=validations.validate_ucsm_name, help="UCSM manager name")
@click.option("--chassis-id", "chassis_id", default='', help="Chassis Id")
@click.option("--chassis-serial", "chassis_serial", default='', help="Chassis serial number")
@click.option("--power", is_flag=True, show_default=True, default=False, help="Power state information")
@click.option("--thermal", is_flag=True, show_default=True, default=False, help="Thermal state information")
@click.option("--env", is_flag=True, show_default=True, default=False, help="Environmental state information")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ucsm_blades_command(
        ctx,
        ucsm,
        chassis_id,
        chassis_serial,
        power,
        thermal,
        env,
        output,
        devel
        ):
    """Get ucsm blades"""

    # iserver get ucsm blades

    ctx.developer = devel

    try:
        if chassis_id == '' and chassis_serial == '':
            ctx.my_output.error('Select chassis by id or serial')
            raise ErrorExit

        if chassis_id != '' and chassis_serial != '':
            ctx.my_output.error('Select chassis by id or serial')
            raise ErrorExit

        ucsm_handler = manager.UcsManager(
            ucsm['ip'],
            ucsm['username'],
            ucsm['password'],
            log_id=ctx.run_id
        )

        if not ucsm_handler.is_connected():
            ctx.my_output.error('Failed to connect to UCSM')
            raise ErrorExit

        if chassis_id == '':
            chassis_id = ucsm_handler.get_chassis_id(
                chassis_serial=chassis_serial
            )
            if chassis_id is None:
                ctx.my_output.error('Failed to find chassis with serial: %s' % (chassis_serial))
                raise ErrorExit

        if not ucsm_handler.is_chassis_id(chassis_id):
            ctx.my_output.error('Failed to find chassis with id: %s' % (chassis_id))
            raise ErrorExit

        chassis_rn = ucsm_handler.get_chassis_property(chassis_id, 'rn')
        if chassis_rn is None:
            ctx.my_output.error('Failed to find chassis name: %s' % (chassis_id))
            raise ErrorExit

        if env:
            power = True
            thermal = True

        blades_info = ucsm_handler.get_blades(
            chassis_rn=chassis_rn,
            power=power,
            thermal=thermal
        )
        if blades_info is None:
            ctx.my_output.error('Failed to get blades info')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    blades_info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(blades_info)

        ucsm_handler.print_blades(
            blades_info,
            power=power,
            thermal=thermal,
            include_chassis_id=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
