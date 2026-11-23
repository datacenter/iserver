import sys
import traceback
import click

from lib.intersight.lcm import tag as lcm_server_tag
from lib.intersight import validations as intersight_validations
from lib.vc import vcenter
from lib.vc import settings as vc_settings

from menu import defaults
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("tag")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--add", "add_tag", multiple=True, callback=intersight_validations.tag, help="Tags to be added")
@click.option("--del", "del_tag", multiple=True, callback=intersight_validations.tag, help="Tags to be deleted")
@click.option("--except", "except_tag", multiple=True, callback=intersight_validations.tag, help="Do not delete")
@click.option("--ip", "ip_filter", multiple=True, help="Select server by IP or subnet")
@click.option("--name", "name_filter", multiple=True, callback=intersight_validations.name_filter, help="Select server by name")
@click.option("--serial", "serial_filter", multiple=True, callback=intersight_validations.serial_filter, help="Select server by serial")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Server group name")
@click.option("--model", "model_filter", multiple=True, callback=intersight_validations.model_filter, help="Select by model")
@click.option("--tag", "tag_filter", multiple=True, callback=intersight_validations.tag_filter, help="Tag filter")
@click.option("--vc", "vcenter_name", default='', help="vCenter name")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_server_tag_command(
        ctx,
        iaccount,
        add_tag,
        del_tag,
        except_tag,
        ip_filter,
        name_filter,
        serial_filter,
        group_filter,
        model_filter,
        tag_filter,
        vcenter_name,
        dry_run,
        devel
    ):
    """Set server tag"""

    # iserver set server tag

    ctx.developer = devel

    try:
        if len(add_tag) == 0 and len(del_tag) == 0:
            ctx.my_output.error(
                'Define tag to be added or deleted'
            )
            raise ErrorExit

        if len(vcenter_name) > 0:
            vc_settings_handler = vc_settings.VcSettings(log_id=ctx.run_id)
            vcenter_settings = vc_settings_handler.get_vc_instance(vcenter_name)
            if vcenter_settings is None:
                ctx.my_output.error('vcenter not found: %s' % (vcenter_name))
                raise ErrorExit

            vc_handler = vcenter.Vcenter(
                vcenter_settings['ip'],
                vcenter_settings['username'],
                vcenter_settings['password'],
                port=vcenter_settings['port'],
                log_id=ctx.run_id
            )

            ctx.my_output.default('Get vcenter hosts...')

            hosts = vc_handler.get_hosts_summary()
            if hosts is None:
                ctx.my_output.error('No hosts found')
                raise ErrorExit

            for host in hosts:
                group_filter.append(
                    host['serial']
                )

        ctx.my_output.default('Get servers...')
        servers_mo = common.get_servers_mo(
            ctx,
            iaccount,
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=intersight_validations.add_group_filter(serial_filter, group_filter),
            model_filter=model_filter,
            tag_filter=tag_filter,
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

        if not lcm_server_tag_handler.set(servers_mo, add_tag, del_tag, except_tag):
            raise ErrorExit

        if not dry_run:
            common.print_servers_info(
                ctx,
                iaccount,
                serial_filter=intersight_validations.get_serial_filter_from_mo(servers_mo),
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
