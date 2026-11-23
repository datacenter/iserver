import sys
import traceback
import click
from menu import validations
from menu.get.k8s import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vastd")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--namespace", default='vast-csi', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--view", "-v", default=['state'], help="[state,manifest]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_vastd_command(
        ctx,
        cluster,
        namespace,
        name,
        view,
        output
        ):
    """Get k8s vast driver"""

    try:
        success = common.get(
            ctx,
            cluster,
            'vast_driver',
            output,
            view,
            'state (def), manifest',
            cluster_type='ocp',
            filter_params=dict(namespace=namespace,name=name),
            get_params=dict(storage_info=True)
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
