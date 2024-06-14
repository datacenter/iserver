import sys
import traceback
import click

from lib.psirt import settings
from lib.psirt import output as psirt_output

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("psirt")
@click.pass_obj
@click.option("--key", default='', callback=validations.empty_string_to_none, help="API key")
@click.option("--secret", default='', callback=validations.empty_string_to_none, help="API secret")
@click.option("--cache", default='', callback=validations.empty_string_to_none, help="Cache on|off")
@click.option("--ttl", default=0, type=click.INT, help="Cache TTL")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_psirt_command(
        ctx,
        key,
        secret,
        cache,
        ttl,
        devel
        ):
    """Set psirt api settings"""

    # iserver set psirt

    ctx.developer = devel

    try:
        settings_handler = settings.PsirtSettings(log_id=ctx.run_id)

        if key is not None and secret is not None:
            success = settings_handler.set_psirt_credentials(
                key,
                secret
            )
            if not success:
                ctx.my_output.error('Failed to set psirt api')
                raise ErrorExit
            ctx.my_output.default('Psirt api access configured')

        if cache.lower() == 'on':
            success = settings_handler.set_cache_on()
            if not success:
                ctx.my_output.error('Failed to enable cache')
                raise ErrorExit
            ctx.my_output.default('Cache enabled')

        if cache.lower() == 'off':
            success = settings_handler.set_cache_off()
            if not success:
                ctx.my_output.error('Failed to disable cache')
                raise ErrorExit
            ctx.my_output.default('Cache disabled')

        if ttl > 0:
            success = settings_handler.set_cache_ttl(ttl)
            if not success:
                ctx.my_output.error('Failed to set cache ttl')
                raise ErrorExit
            ctx.my_output.default('Cache ttl set')

        psirt_settings = settings_handler.get_psirt_settings()
        if psirt_settings is None:
            ctx.my_output.error('Failed to get psirt api settings')
            raise ErrorExit

        output_handler = psirt_output.PsirtOutput(log_id=ctx.run_id)

        output_handler.print_psirt_settings(
            psirt_settings,
            show_password=False
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
