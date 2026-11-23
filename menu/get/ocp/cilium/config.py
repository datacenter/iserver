import sys
import click
from menu import validations
from lib.workflow.ocp_cilium_cni import get_config as get


@click.command("config")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--view", "-v", default=['config'], help="[config|map|state|all]", show_default=True, multiple=True)
def get_ocp_cilium_config_command(ctx, cluster_names, view):
    """Get cilium configuration"""

    params = {}
    params['cluster'] = cluster_names
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View (-v): config (def), map, state, all', before_newline=True)