import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_identity_htpasswd import delete as ocp_delete_workflow


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("htpasswd")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name, type=click.STRING, help="Cluster Name")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="HTPasswd Provider Name")
@click.option("--filename", "htpasswd_filename", multiple=True, help="htpasswd filename")
@click.option("--user", "users", is_flag=False, multiple=True, help="Usernames")
@click.option("--admin", "admins", is_flag=False, multiple=True, help="Admin users")
def delete_ocp_htpasswd_command(ctx, cluster_name, provider_name, htpasswd_filename, users, admins):
    """Delete identity htpasswd in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['provider'] = provider_name
        params['filename'] = htpasswd_filename
        params['userpass'] = users
        params['admins'] = admins
        params['mode'] = 'delete'

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
