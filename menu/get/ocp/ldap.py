import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_identity_ldap import get as ocp_installer

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ldap")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--view", "-v", default=['list'], help="[list|verbose]", show_default=True, multiple=True)
def get_ocp_ldap_command(ctx, cluster_name, view):
    """Get identity ldap in openshift cluster"""

    view = validations.validate_view(
        ctx,
        view,
        'list|verbose',
        'list',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        params = {}
        params['cluster'] = cluster_name
        params['view'] = view

        success = ocp_installer.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('View: list (def), verbose', before_newline=True)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
