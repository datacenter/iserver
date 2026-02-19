import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_inb import get


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("inb")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--vc", "vcenter", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--view", "-v", default=['all'], help="[ssh|vc|kube|pnet|mesh|all]", show_default=True, multiple=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
def get_ocp_cilium_inb_command(ctx, cluster_name, vcenter, mesh_name, view, verbose):
    """Get isovalent network bridge"""

    view = validations.validate_view(
        ctx,
        view,
        'ssh|vc|kube|pnet|mesh|all',
        'state',
        []
    )

    try:
        params = {}
        params['cluster'] = cluster_name
        params['vcenter'] = vcenter
        params['mesh-name'] = mesh_name
        params['view'] = view
        params['verbose'] = verbose

        success = get.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit         
            
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
