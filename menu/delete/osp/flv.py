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


@click.command("flv")
@click.pass_obj
@click.option("--cluster", default='', help="OpenStack cluster name")
@click.option("--id", "flavor_id", default='', callback=validations.empty_string_to_none, help="Flavor id")
@click.option("--name", "flavor_name", default='', callback=validations.empty_string_to_none, help="Flavor name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_flv_command(
        ctx,
        cluster,
        flavor_id,
        flavor_name,
        no_confirm
        ):
    """Delete osp flavor"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        if flavor_id is None and flavor_name is None:
            flavors = osp_handlers.get_flavors()
            flavor_info = osp_output_handler.select_flavor(flavors)
            if flavor_info is None:
                raise ErrorExit

        if flavor_id is not None:
            flavor_info = osp_handlers.get_flavor(
                flavor_id=flavor_id
            )
            if flavor_info is None:
                ctx.my_output.error('Flavor not found by id')
                raise ErrorExit

        if flavor_name is not None:
            flavor_info = osp_handlers.get_flavor(
                flavor_name=flavor_name
            )
            if flavor_info is None:
                ctx.my_output.error('Flavor not found by name')
                raise ErrorExit

        ctx.my_output.default('Delete flavor %s [%s]' % (flavor_info['name'], flavor_info['id']))
        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        success = osp_handlers.delete_flavor_mo(flavor_info['id'])
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
