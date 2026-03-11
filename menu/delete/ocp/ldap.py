import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_identity_ldap import delete as ocp_delete_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ldap")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name, type=click.STRING, help="Cluster Name")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="HTPasswd Provider Name")
@click.option("--no-deps", is_flag=True, show_default=True, default=False, help="OAuth delete only")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_ldap_command(ctx, cluster_name, provider_name, no_deps, no_confirm):
    """Delete identity ldap in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['provider'] = provider_name
        params['dependencies'] = not no_deps
        params['confirmation'] = not no_confirm

        success = ocp_delete_workflow.run(
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
