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


@click.command("sub")
@click.pass_obj
@click.option("--cluster", default='', help="OpenStack cluster name")
@click.option("--id", "subnet_id", default='', callback=validations.empty_string_to_none, help="Subnet id")
@click.option("--name", "subnet_name", default='', callback=validations.empty_string_to_none, help="Subnet name")
@click.option("--network-name", "network_name", default='', callback=validations.empty_string_to_none, help="Filter by network name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_sub_command(
        ctx,
        cluster,
        subnet_id,
        subnet_name,
        network_name,
        no_confirm
        ):
    """Delete osp subnet"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        if subnet_id is None and subnet_name is None:
            object_filter = []
            if network_name is not None:
                object_filter.append('network_name:%s' % (network_name))

            subnets = osp_handlers.get_subnets(
                object_filter=object_filter,
                tenant_info=True,
                network_info=True
            )
            subnet_info = osp_output_handler.select_subnet(subnets)
            if subnet_info is None:
                raise ErrorExit

            subnet_id = subnet_info['id']
            subnet_name = subnet_info['name']

        if subnet_id is not None:
            subnet_info = osp_handlers.get_subnet(
                subnet_id=subnet_id
            )
            if subnet_info is None:
                ctx.my_output.error('Subnet not found by id')
                raise ErrorExit

            subnet_name = subnet_info['name']

        if subnet_id is None and subnet_name is not None:
            subnet_info = osp_handlers.get_subnet(
                subnet_name=subnet_name
            )
            if subnet_info is None:
                ctx.my_output.error('Subnet not found by name')
                raise ErrorExit

        ctx.my_output.default('Delete subnet %s [%s]' % (subnet_info['name'], subnet_info['id']))
        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        success = osp_handlers.delete_subnet_mo(subnet_id)
        if not success:
            ctx.my_output.error('Failed')
            raise ErrorExit

        ctx.my_output.default('Deleted')

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
