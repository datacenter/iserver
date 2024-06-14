import sys
import threading
import traceback
import click

from lib.redfish import cache

from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cache")
@click.pass_obj
@click.option("--name", "custom_cache_name", default='', help="Cache entry name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_redfish_cache_command(
        ctx,
        custom_cache_name,
        devel
        ):
    """Delete redfish endpoint cache"""

    # iserver delete redfish cache

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if custom_cache_name == '':
            ctx.my_output.error('Define cache entry name')
            raise ErrorExit

        redfish_cache_handler = cache.RedfishCache()
        if custom_cache_name == 'all':
            success = redfish_cache_handler.delete_redfish_cache_entries()
            if not success:
                ctx.my_output.error('All cache entries delete failed')
                raise ErrorExit

            ctx.my_output.default('All cache entries deleted')

        else:
            success = redfish_cache_handler.delete_redfish_cache_entry(custom_cache_name)
            if not success:
                ctx.my_output.error('Cache entry delete failed')
                raise ErrorExit

            ctx.my_output.default('Cache entry deleted: %s' % (custom_cache_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
