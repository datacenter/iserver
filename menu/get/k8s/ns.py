import sys
import traceback
import click

from menu.get.k8s import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ns")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--view", "-v", default=['state'], help="[state|res|udn]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_ns_command(
        ctx,
        cluster,
        name,
        view,
        output
        ):
    """Get k8s namespace"""

    try:
        res_info = False
        if 'res' in view:
            res_info = True

        success = common.get(
            ctx,
            cluster,
            'namespace',
            output,
            view,
            'state (def), res, udn',
            filter_params=dict(name=name),
            get_params=dict(res_info=res_info)
        )
        if not success:
            raise ErrorExit
        
    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
