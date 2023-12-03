import sys
import traceback
import click

from lib.lcm_server import tag as lcm_server_tag

from menu import defaults
from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("tag")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--ip", "ip_filter", multiple=True, help="Select by IP or subnet")
@click.option("--name", "name_filter", multiple=True, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, help="Select by serial")
@click.option("--tag", default=[], help="key:value tag", show_default=True, multiple=True)
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_server_tag_command(
        ctx,
        iaccount,
        group_filter,
        serial_filter,
        name_filter,
        ip_filter,
        tag,
        dry_run,
        devel
        ):
    """Delete server tag"""

    # iserver set server tag

    ctx.developer = devel

    try:
        if len(tag) == 0:
            ctx.my_output.error(
                'Define tag to be deleted'
            )
            raise ErrorExit

        for item in tag:
            if len(item.split(':')) != 2:
                ctx.my_output.error(
                    'Define tag in key:value format'
                )
                raise ErrorExit

            if len(item.split(':')[0]) == 0:
                ctx.my_output.error(
                    'Define tag in key:value format'
                )
                raise ErrorExit

            if len(item.split(':')[1]) == 0:
                ctx.my_output.error(
                    'Define tag in key:value format'
                )
                raise ErrorExit

        new_serial_filter = []
        for item in group_filter:
            new_serial_filter.append(item)
        for item in serial_filter:
            new_serial_filter.append(item)

        servers_mo = common.get_servers_mo(
            ctx,
            iaccount,
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=new_serial_filter,
            include_rack=True,
            include_blade=True,
            show_progress=True
        )
        if servers_mo is None or len(servers_mo) == 0:
            ctx.my_output.error(
                'No servers matching search criteria'
            )
            raise ErrorExit

        common.print_servers_mo_info(
            ctx,
            iaccount,
            servers_mo,
            show_progress=True,
            cache=False
        )

        if not common.get_confirmation():
            return

        lcm_server_tag_handler = lcm_server_tag.LcmServerTag(
            iaccount,
            dry_run=dry_run,
            wait=True,
            silent=False,
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )
        if not lcm_server_tag_handler.delete(servers_mo, tag):
            raise ErrorExit

        common.print_servers_info(
            ctx,
            iaccount,
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=new_serial_filter,
            include_rack=True,
            include_blade=True,
            show_progress=True,
            cache=False
        )

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
