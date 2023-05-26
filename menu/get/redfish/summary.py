import sys
import json
import threading
import traceback
import click

from progress.bar import Bar

from lib.redfish import endpoint_settings

from menu import common
from menu import defaults
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("summary")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify endpoint")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_summary_command(
        ctx,
        iaccount,
        verify,
        output,
        devel
        ):
    """Get intersight inventory redfish access summary"""

    # iserver get redfish summary

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        bar_enabled = False
        if output == 'default':
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()
            bar_enabled = True

        servers = common.get_servers(
            ctx,
            iaccount,
            locator=False,
            server_setting_id=False,
            workflow=None,
            registration=False
        )
        if servers is None or len(servers) == 0:
            ctx.my_output.default('No servers found')
            return

        endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
            log_id=ctx.run_id
        )
        servers = endpoint_settings_handler.get_servers_redfish_settings(
            servers,
            verify=verify,
            bar_enabled=bar_enabled
        )

        summary = endpoint_settings_handler.get_servers_redfish_summary(
            servers,
            verify=verify
        )

        if output == 'json':
            ctx.my_output.default(json.dumps(summary, indent=4))
            return

        endpoint_settings_handler.print_servers_redfish_summary(
            summary,
            verify=verify
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
