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
@click.option("--id", "network_id", default='', callback=validations.empty_string_to_none, help="Network id")
@click.option("--name", "network_name", default='', callback=validations.empty_string_to_none, help="Network name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_net_command(
        ctx,
        cluster,
        network_id,
        network_name,
        no_confirm
        ):
    """Delete osp network"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        if network_id is None and network_name is None:
            networks = osp_handlers.get_networks()
            network_info = osp_output_handler.select_network(networks)
            if network_info is None:
                raise ErrorExit

            network_id = network_info['id']
            network_name = network_info['name']

        if network_id is not None:
            network_info = osp_handlers.get_network(
                network_id=network_id
            )
            if network_info is None:
                ctx.my_output.error('Network not found by id')
                raise ErrorExit

        if network_name is not None:
            network_info = osp_handlers.get_network(
                network_name=network_name
            )
            if network_info is None:
                ctx.my_output.error('Network not found by name')
                raise ErrorExit

        ctx.my_output.default('Delete network %s [%s]' % (network_info['name'], network_info['id']))
        for subnet_info in network_info['subnet_info']:
            ctx.my_output.default('Delete subnet %s [%s]' % (subnet_info['name'], subnet_info['id']))

        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        for subnet_info in network_info['subnet_info']:
            success = osp_handlers.delete_subnet_mo(subnet_info['id'])
            if not success:
                ctx.my_output.error('Subnet delete failed: %s' % (subnet_info['id']))
                raise ErrorExit

        success = osp_handlers.delete_network_mo(network_id)
        if not success:
            ctx.my_output.error('Network delete failed')
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
