import sys
import traceback
import click
from menu.get.k8s import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("lv")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_lv_command(
        ctx,
        cluster,
        view,
        output
        ):
    """Get k8s logical volume"""

    try:
        success = common.get(
            ctx,
            cluster,
            'logical_volume',
            output,
            view,
            'state',
            cluster_type='ocp'
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
