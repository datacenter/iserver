import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cnv_operator import get_operator
from lib.workflow.ocp_cnv_operator import get_crd
from lib.workflow.ocp_cnv_operator import get_import

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cnv")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['state'], show_default=True, multiple=True, help="Scope of output (view): [state|import|crd]")
def get_ocp_cnv_command(ctx, cluster_name, view):
    """Get cnv operator in openshift cluster"""

    view = validations.validate_view(
        ctx,
        view,
        'state|import|crd',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        if 'state' in view:
            params = {}
            params['cluster'] = cluster_name
            
            success = get_operator.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
        
        if 'crd' in view:
            params = {}
            params['cluster'] = cluster_name
            
            success = get_crd.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if 'import' in view:
            params = {}
            params['cluster'] = cluster_name
            
            success = get_import.run(
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
