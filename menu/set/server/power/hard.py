import sys
import copy
import traceback
import click

from lib.lcm_server import power as lcm_server_power
from menu import defaults
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("hard")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial numbers")
@click.option("--name", "name_filter", default='', help="Name loose match")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_server_power_hard_command(ctx, iaccount, group, serial_filter, name_filter, ip_filter, no_confirm, dry_run, verbose, no_wait, devel):
    """Hard reset"""

    # iserver set server power hard

    ctx.developer = devel
    silent = False
    debug = False
    common.flags_fixup(ctx, silent, verbose, debug)

    try:
        servers = common.get_selected_servers(
            ctx,
            iaccount,
            group,
            serial_filter,
            name_filter,
            ip_filter,
            confirm=not no_confirm
        )
        if servers is None or len(servers) == 0:
            raise ErrorExit

        powered_off = False
        for server in servers:
            if server['OperPowerState'] != 'on':
                powered_off = True

        if powered_off:
            ctx.my_output.default('Some servers are powered off. Hard reset will fail on those servers. Remove powered-off servers from the list?')
            if not no_confirm or common.get_confirmation():
                new_servers = []
                for server in servers:
                    if server['OperPowerState'] != 'on':
                        ctx.my_output.default('Server %s removed' % (server['Name']))
                        continue
                    new_servers.append(server)
                servers = copy.deepcopy(new_servers)

        lcm_server_power_handler = lcm_server_power.LcmServerPower(
            iaccount,
            dry_run=dry_run,
            wait=not no_wait,
            silent=silent,
            verbose=verbose,
            debug=debug,
            log_id=ctx.run_id
        )
        if not lcm_server_power_handler.power_hard(servers):
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
