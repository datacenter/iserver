import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("ldap")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="HTPasswd Provider Name")
@click.option("--no-deps", is_flag=True, show_default=True, default=False, help="OAuth delete only")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_ldap_command(ctx, cluster_names, provider_name, no_deps, no_confirm):
    """Delete identity ldap in openshift cluster"""

    task = {}
    task['feature'] = {}
    task['feature']['provider'] = provider_name
    task['feature']['dependencies'] = not no_deps

    success = ocp_common.delete_workflow(cluster_names, 'identity-ldap', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)