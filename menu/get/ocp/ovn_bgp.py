import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_ovn_bgp import get as ocp_workflow

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ovn-bgp")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--node", multiple=True, help="Select nodes by name")
@click.option("--peer", multiple=True, help="Select peers by ip")
@click.option("--cmd", default='', callback=validations.empty_string_to_none, help="Exec command")
@click.option("--view", "-v", default=['state'], help="[state|cli|config|exec|frr|ra|ra-config|session|all]", show_default=True, multiple=True)
def get_ocp_ovn_bgp_command(ctx, cluster_name, node, peer, cmd, view):
    """Get ocp ovn bgp"""

    view = validations.validate_view(
        ctx,
        view,
        'state|cli|config|exec|frr|ra|ra-config|session|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)
    
    try:
        params = {}
        params['cluster'] = cluster_name
        params['node'] = []
        for item in node:
            params['node'].append(item)
        params['peer'] = []
        for item in peer:
            params['peer'].append(item)
        params['cmd'] = cmd
        params['view'] = view

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default(
            'View: state (def), cli, config, exec, frr, ra, ra-config, session, all',
            before_newline=True
        )
        
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
