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


@click.command("boot-device")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="Management IP address")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--type", "device_type", callback=imc_validations.validate_boot_device_type, help="Device type")
@click.option("--name", "device_name", help="Device name")
@click.option("--order", "device_order", help="Device order")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_imc_cli_boot_device_command(
        ctx,
        endpoint_ip,
        username,
        password,
        device_type,
        device_name,
        device_order,
        devel
        ):
    """Set boot device"""

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

            success = endpoint_handler.create_boot_device(
                device_name,
                device_type,
                device_order=device_order
            )
            if not success:
                ctx.my_output.error('Failed to create boot device: %s' % (item['ip']))
                raise ErrorExit

            ctx.my_output.default(
                'Boot device created: %s' % (
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
