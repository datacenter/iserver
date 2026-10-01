import sys
import click
from menu import validations
from lib.workflow.ocp_metallb import get


@click.command("metallb")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--node", multiple=True, help="Select nodes by name")
@click.option("--peer", multiple=True, help="Select peers by ip")
@click.option("--cmd", default='', callback=validations.empty_string_to_none, help="Exec command")
@click.option("--view", "-v", default=['state'], help="[state|cli|crd|exec|frr|all]", show_default=True, multiple=True)
def get_ocp_metallb_command(ctx, cluster_names, node, peer, cmd, view):
    """Get metallb operator in openshift cluster"""

    params = {}
    params['cluster'] = cluster_names
    params['node'] = []
    params['peer'] = []
    params['cmd'] = cmd
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default(
        'View: state (def), cli, crd, exec, frr, all',
        before_newline=True
    )