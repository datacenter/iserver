import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("htpasswd")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="HTPasswd Provider Name")
@click.option("--filename", "htpasswd_filename", multiple=True, help="htpasswd filename")
@click.option("--user", "users", is_flag=False, multiple=True, help="Usernames")
@click.option("--admin", "admins", is_flag=False, multiple=True, help="Admin users")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_htpasswd_command(ctx, cluster_names, provider_name, htpasswd_filename, users, admins, no_confirm):
    """Delete identity htpasswd in openshift cluster"""

    task = {}
    task['instance'] = {}
    task['instance']['provider'] = provider_name
    task['instance']['filename'] = htpasswd_filename
    task['instance']['userpass'] = users
    task['instance']['admins'] = admins
    task['instance']['mode'] = 'delete'

    success = ocp_common.delete_workflow(cluster_names, 'identity-htpasswd', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)