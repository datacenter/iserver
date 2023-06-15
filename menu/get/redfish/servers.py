import sys
import json
import threading
import traceback
import click

from lib.redfish import endpoint_settings

from menu import common
from menu import defaults
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("servers")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial strict match filter")
@click.option("--model", "model_filter", default='', help="Model loose match filter")
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify endpoint")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_redfish_servers_command(
        ctx,
        iaccount,
        group,
        ip_filter,
        name_filter,
        serial_filter,
        model_filter,
        show_password,
        verify,
        output,
        devel
        ):
    """Get intersight servers redfish access configuration"""

    # iserver get redfish servers

    ctx.developer = devel
    common.flags_fixup(ctx, False, False, False)

    try:
        if output == 'json':
            bar_enabled = False

        if output == 'default':
            bar_enabled = True
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        servers = common.get_selected_servers(
            ctx,
            iaccount,
            group,
            serial_filter,
            name_filter,
            ip_filter,
            model_filter=model_filter,
            confirm=False,
            workflow=None,
            server_setting_id=False,
            locator=False,
            registration=False,
            show_servers=False,
            allow_all=True
        )
        if servers is None or len(servers) == 0:
            ctx.my_output.default('No servers found')
            return

        endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
            log_id=ctx.run_id
        )
        servers = endpoint_settings_handler.get_servers_redfish_settings(servers, verify=verify, bar_enabled=bar_enabled)

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    servers,
                    indent=4
                )
            )
            return

        endpoint_settings_handler.print_servers_redfish(
            servers,
            verify=verify,
            show_password=show_password
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
