import sys
import traceback
import click

from lib.redfish import cache


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
        cache_handler = cache.RedfishCache()
        cache_handler.print_redfish_cache()

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
