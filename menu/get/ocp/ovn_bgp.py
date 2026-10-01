import sys
import click
from menu import validations
from lib.workflow.ocp_ovn_bgp import get


@click.command("ovn-bgp")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--node", multiple=True, help="Select nodes by name")
@click.option("--peer", multiple=True, help="Select peers by ip")
@click.option("--cmd", default='', callback=validations.empty_string_to_none, help="Exec command")
@click.option("--view", "-v", default=['state'], help="[state|cli|config|exec|frr|ra|ra-config|session|all]", show_default=True, multiple=True)
def get_ocp_ovn_bgp_command(ctx, cluster_names, node, peer, cmd, view):
    """Get ocp ovn bgp"""

    params = {}
    params['cluster'] = cluster_names
    params['node'] = node
    params['peer'] = peer
    params['cmd'] = cmd
    params['view'] = view

    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    ctx.my_output.default(
        'View: state (def), cli, config, exec, frr, ra, ra-config, session, all',
        before_newline=True
    )