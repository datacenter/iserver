import sys
import traceback
import click

from lib.redfish import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("settings")
@click.pass_obj
def get_redfish_settings_command(ctx):
    """Get redfish settings"""

    # iserver get redfish settings

    try:
        settings_handler = settings.RedfishSettings()
        settings_handler.print_redfish_settings()

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
