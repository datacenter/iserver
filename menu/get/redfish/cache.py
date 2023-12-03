import sys
import traceback
import click

from lib.redfish import cache
from lib.redfish import output as redfish_output
from lib.redfish import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cache")
@click.pass_obj
def get_redfish_cache_command(ctx):
    """Get redfish cache"""

    # iserver get redfish cache

    try:
        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)

        settings_handler = settings.RedfishSettings()
        redfish_settings = settings_handler.get_redfish_settings()
        output_handler.print_redfish_settings(redfish_settings)

        cache_handler = cache.RedfishCache()
        info = cache_handler.get_redfish_cache_list()
        if info is None:
            ctx.my_output.error('Cache list not found')
            raise ErrorExit

        output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)
        output_handler.print_redfish_cache(
            info,
            title=True
        )

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
