import sys
import click
from menu import validations
from lib.workflow.ocp_iotel import get


@click.command("iotel")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--suffix", default='', callback=validations.empty_string_to_none, help="Select suffix by name")
@click.option("--view", "-v", default=['state'], help="[state|poller|res|all]", show_default=True, multiple=True)
def get_ocp_iotel_command(ctx, cluster_names, suffix, view):
    """Get openshift intersight open telemetry collector"""

    params = {}
    params['cluster'] = cluster_names
    params['suffix'] = suffix
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default('View: state (def), poller, res, all', before_newline=True)