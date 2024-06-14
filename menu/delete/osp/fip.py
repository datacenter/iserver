import sys
import traceback
import click

from lib import ip_helper
from lib.osp import output as osp_output

from menu import common
from menu import validations



class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("fip")
@click.pass_obj
@click.option("--cluster", default='', help="OpenStack cluster name")
@click.option("--ip", "floating_ip_address", default='', callback=validations.validate_ip, help="Select by floating address")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_fip_command(
        ctx,
        cluster,
        floating_ip_address,
        no_confirm
        ):
    """Delete osp fip"""

    # iserver delete osp fip

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        object_filter = []

        if len(floating_ip_address) == 0:
            fips = osp_handlers.get_floating_ips(
                object_filter=object_filter,
                tenant_info=True,
                network_info=True,
                router_info=True,
                port_info=True
            )

            osp_output_handler.print_floating_ips(
                fips,
                title=True
            )

            floating_ip_address = input("Define floating IP to be deleted: ")
            if not ip_helper.is_valid_ipv4_address(floating_ip_address):
                ctx.my_output.error('Invalid IPv4 address')
                raise ErrorExit

        floating_ip_info = osp_handlers.get_floating_ip(
            floating_ip=floating_ip_address
        )

        if floating_ip_info is None:
            ctx.my_output.error('Failed to get floating IP details')
            raise ErrorExit

        osp_output_handler.print_floating_ips(
            [floating_ip_info],
            title=False
        )

        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        if not osp_handlers.delete_floating_ip_mo(floating_ip_info['id']):
            ctx.my_output.error('Failed to delete floating IP')
            raise ErrorExit

        ctx.my_output.default('Floating IP deleted')

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
