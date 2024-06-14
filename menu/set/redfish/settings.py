import os
import sys
import traceback
import click

from lib.redfish import settings
from lib.redfish import output as redfish_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("settings")
@click.pass_obj
@click.option("--cache-enable", is_flag=True, show_default=True, default=False, help="Enable cache")
@click.option("--cache-disable", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--cache-dir", "cache_directory", is_flag=False, show_default=False, default='', type=click.STRING, help="Cache directory")
def set_redfish_settings_command(ctx, cache_directory, cache_enable, cache_disable):
    """Set redfish settings"""

    # iserver get redfish settings

    try:
        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)
        settings_handler = settings.RedfishSettings()

        redfish_settings = settings_handler.get_redfish_settings()
        if redfish_settings is None:
            ctx.my_output.error('Settings get failed')
            raise ErrorExit

        if len(cache_directory) > 0:
            if not os.path.isabs(cache_directory):
                ctx.my_output.error('Cache directory must be absolute path')
                raise ErrorExit

            redfish_settings['CacheDirectory'] = cache_directory
            if not os.path.isdir(cache_directory):
                os.makedirs(cache_directory, exist_ok=True)
                ctx.my_output.default('Cache directory created: %s' % (cache_directory))

        if cache_enable:
            redfish_settings['CacheEnabled'] = True

        if cache_disable:
            redfish_settings['CacheEnabled'] = False

        if not settings_handler.set_redfish_settings(redfish_settings):
            ctx.my_output.error('Settings set failed')
            raise ErrorExit

        redfish_settings = settings_handler.get_redfish_settings()
        output_handler.print_redfish_settings(redfish_settings)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
