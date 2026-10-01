import sys
import click
from menu import validations
from lib.workflow import ocp_common
from menu import user_inputs


@click.command("htpasswd")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="HTPasswd Provider Name")
@click.option("--filename", "htpasswd_filename", multiple=True, help="htpasswd filename")
@click.option("--user", "userpass", is_flag=False, multiple=True, help="User:pass entries")
@click.option("--admin", "admins", is_flag=False, multiple=True, help="Admin users")
@click.option("--mode", type=click.Choice(['post', 'patch'], case_sensitive=False), default='patch', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_htpasswd_command(ctx, cluster_names, provider_name, htpasswd_filename, userpass, admins, mode, no_confirm):
    """Set identity htpasswd in openshift cluster"""

    if provider_name is None:
        provider_name = user_inputs.get_value(ctx, prompt='Provider name', empty=True)
        if len(provider_name) == 0:
            sys.exit(1)

    if len(htpasswd_filename) == 0 and len(userpass) == 0 and len(admins) == 0:
        value = user_inputs.get_value(ctx, prompt='htpasswd file (comma-seperated)', empty=True)
        if len(value) > 0:
            htpasswd_filename = value.split(',')

        value = user_inputs.get_value(ctx, prompt='user:pass (comma-separated)', empty=True)
        if len(value) > 0:
            userpass = value.split(',')
            value = user_inputs.get_value(ctx, prompt='admins (comma-separated or __ALL__)', empty=True)
            if len(value) > 0:
                admins = value.split(',')

    task = {}
    task['instance'] = {}
    task['instance']['provider'] = provider_name
    task['instance']['filename'] = htpasswd_filename
    task['instance']['userpass'] = userpass
    task['instance']['admins'] = admins
    task['instance']['mode'] = mode

    success = ocp_common.set_workflow(cluster_names, 'identity-htpasswd', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)