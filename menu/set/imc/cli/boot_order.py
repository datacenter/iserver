import sys
import traceback
import click

from lib.imc.cli import endpoint

from menu import common
from menu import validations
from menu.get.imc.cli import validations as imc_validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("boot-order")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="Management IP address")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--device", multiple=True, callback=imc_validations.validate_boot_order, help="Device order: hdd, pxe, fdd, efi, cdrom")
@click.option("--reboot", is_flag=True, show_default=True, default=False, help="Perform reboot")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_imc_cli_boot_order_command(
        ctx,
        endpoint_ip,
        username,
        password,
        device,
        reboot,
        devel
        ):
    """Set boot order"""

    # iserver set imc cli endpoint

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        endpoints = imc_validations.get_imc_cli_endpoints(
            ctx,
            endpoint_ip,
            username,
            password
        )

        if endpoints is None:
            raise ErrorExit

        if len(endpoints) == 0:
            ctx.my_output.error('Define imc endpoints')
            raise ErrorExit

        for item in endpoints:
            endpoint_handler = endpoint.ImcCliEndpoint(
                item['ip'],
                item['port'],
                item['username'],
                item['password'],
                cache_ttl=-1,
                log_id=ctx.run_id
            )

            success = endpoint_handler.set_boot_order(
                device
            )
            if not success:
                ctx.my_output.error('Failed to set boot order for: %s' % (item['ip']))
                raise ErrorExit

            ctx.my_output.default(
                'Boot order set for endpoint %s: %s' % (
                    item['ip'],
                    ','.join(device)
                )
            )

            if reboot:
                success = endpoint_handler.power_cycle()
                if not success:
                    ctx.my_output.error('Failed to power cycle server: %s' % (item['ip']))
                    raise ErrorExit

                ctx.my_output.default(
                    'Server power cycle successful: %s' % (
                        item['ip']
                    )
                )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
