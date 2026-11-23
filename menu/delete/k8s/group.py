import sys
import click
import traceback

from menu import validations
from lib.workflow.ocp_oauth import group_delete as workflow


class ErrorExit(Exception):
    pass


@click.command("group")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Select by group name")
@click.option("--ldap-host", default='', callback=validations.empty_string_to_none, help="Synced from ldap host")
@click.option("--ldap", is_flag=True, show_default=True, default=False, help="Synced from ldap")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_k8s_group_command(
        ctx,
        cluster_name,
        name,
        ldap_host,
        ldap,
        no_confirm
        ):
    """Delete k8s group"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        params = {}
        params['cluster'] = cluster_name
        params['group'] = name
        params['ldap_host'] = ldap_host
        params['ldap'] = ldap
        params['confirmation'] = not no_confirm

        success = workflow.run(
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
    