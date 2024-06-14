import sys
import traceback
import click

from progress.bar import Bar

from lib.ucsm import manager
from lib.ucsm import endpoint_settings

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("inventory")
@click.pass_obj
@click.option("--manager", "ucsm", default='', callback=validations.validate_ucsm_name, help="UCSM manager name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ucsm_inventory_command(
        ctx,
        ucsm,
        devel
        ):
    """Set ucsm inventory access"""

    # iserver set ucsm inventory

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

        failed = []

        chassiz = ucsm_handler.get_chassiz()
        if chassiz is None:
            ctx.my_output.error('No chassis found')
            raise ErrorExit

        bar_handler = Bar('Chassis', max=len(chassiz))
        bar_handler.goto(0)
        for chassis in chassiz:
            endpoint_settings_handler = endpoint_settings.UcsmEndpointSettings()
            success = endpoint_settings_handler.set_ucsm_endpoint_settings(
                chassis,
                ucsm
            )
            if not success:
                failed.append(
                    dict(
                        type='Chassis',
                        serial=chassis['serial']
                    )
                )

            bar_handler.next()

        bar_handler.finish()

        blades = ucsm_handler.get_blades()
        if blades is None:
            ctx.my_output.error('No blades found')
            raise ErrorExit

        bar_handler = Bar('Blade', max=len(blades))
        bar_handler.goto(0)
        for blade in blades:
            endpoint_settings_handler = endpoint_settings.UcsmEndpointSettings()
            success = endpoint_settings_handler.set_ucsm_endpoint_settings(
                blade,
                ucsm
            )
            if not success:
                failed.append(
                    dict(
                        type='Blade',
                        serial=blade['serial']
                    )
                )

            bar_handler.next()

        bar_handler.finish()

        if len(failed) == 0:
            ctx.my_output.default('All UCSM-attached endpoints settings saved')
            return

        ctx.my_output.default('')
        ctx.my_output.error('Not all UCSM-attached  endpoints settings saved')
        for item in failed:
            ctx.my_output.default('- Type [%s] Serial [%s]' % (item['type'], item['serial']))
        raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
