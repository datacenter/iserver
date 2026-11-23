import sys
import traceback
import click

from menu.get.k8s import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("dep")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--owner", default='', callback=validations.empty_string_to_none, help="Filter by owner")
@click.option("--view", "-v", default=['state'], help="[state|metadata|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_dep_command(
        ctx,
        cluster,
        namespace,
        name,
        owner,
        view,
        output
        ):
    """Get k8s deployment"""

    try:
        success = common.get(
            ctx,
            cluster,
            'deployment',
            output,
            view,
            'state (def), metadata',
            cluster_type='ocp',
            filter_params=dict(namespace=namespace,name=name,owner=owner)
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
