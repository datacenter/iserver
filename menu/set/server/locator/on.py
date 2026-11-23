import sys
import traceback
import click

from lib import ip_helper
from lib.intersight import compute
from lib.intersight import compute_output
from lib.intersight.lcm import locator as lcm_server_locator

from menu import defaults
from menu import validations
from menu import common
from menu import user_inputs


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("on")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--serial", "serial_filter", multiple=True, help="Serial numbers")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Select by group name")
@click.option("--name", "name_filter", multiple=True, help="Name loose match")
@click.option("--ip", "ip_filter", multiple=True, help="Management IP address or subnet filter")
@click.option("--confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_server_locator_on_command(
        ctx,
        iaccount,
        serial_filter,
        group_filter,
        name_filter,
        ip_filter,
        confirm,
        no_wait,
        dry_run,
        verbose,
        devel
    ):
    """Locator on"""

    # iserver set server locator on

    ctx.developer = devel
    silent = False
    debug = False
    common.flags_fixup(ctx, silent, verbose, debug)

    try:
        if len(name_filter) == 0 and len(ip_filter) == 0 and len(serial_filter) == 0 and len(group_filter) == 0:
            server_selection_mode = user_inputs.get_selection(
                ctx,
                'Select server selection type',
                ['name', 'serial', 'ip']
            )

            if server_selection_mode == 'name':
                name_filter = [user_inputs.get_value(ctx, 'Server name')]

            if server_selection_mode == 'serial':
                serial_filter=[user_inputs.get_value(ctx, 'Server serial number')]

            if server_selection_mode == 'ip':
                ip_address = user_inputs.get_value(ctx, 'Server management IP address')
                if not ip_helper.is_valid_ipv4_address(ip_address):
                    ctx.my_output.error('Invalid IPv4 address')
                    raise ErrorExit

                ip_filter = [ip_address]

        serials = []
        for item in serial_filter:
            serials = serials + item.split(',')
        for item in group_filter:
            serials.append(item)

        servers_mo = common.get_servers_mo(
            ctx,
            iaccount,
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=serials,
            show_progress=True,
            include_rack=True,
            include_blade=True,
            rack_expand=['LocatorLed'],
            blade_expand=['LocatorLed']
        )
        if servers_mo is None or len(servers_mo) == 0:
            raise ErrorExit

        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
        compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)

        settings = {}
        settings['state'] = True
        settings['locator'] = True
        settings['workflow'] = None
        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            {},
            1,
            prepare_cache=False
        )

        compute_output_handler.print_summary_table(
            servers_info,
            title=True
        )

        ctx.my_output.default('')

        if confirm:
            if not common.get_confirmation():
                raise ErrorExit

        lcm_server_locator_handler = lcm_server_locator.LcmServerLocator(
            iaccount,
            dry_run=dry_run,
            wait=not no_wait,
            silent=silent,
            verbose=verbose,
            debug=debug,
            log_id=ctx.run_id
        )
        if not lcm_server_locator_handler.locator_on(servers_mo):
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
