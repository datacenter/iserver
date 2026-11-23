import sys
import traceback
import click

from menu.get.k8s import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cudn")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--topology", type=click.Choice(['any', 'l2', 'l3', 'localnet'], case_sensitive=False), default='any', show_default=True)
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_cudn_command(
        ctx,
        cluster,
        name,
        topology,
        view,
        output
        ):
    """Get k8s cluster user defined network"""

    try:
        success = common.get(
            ctx,
            cluster,
            'cluster_user_defined_network',
            output,
            view,
            'state',
            cluster_type='ocp',
            filter_params=dict(name=name,topology=topology),
            get_params=dict(nad_info=True, usage_info=True),
            extra_output=['Legend: (C)reated, (P)rimary']
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
