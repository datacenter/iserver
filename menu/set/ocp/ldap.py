import sys
import click
from menu import validations
from lib.workflow import ocp_common
from menu import user_inputs


@click.command("ldap")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--filename", "ldap_filename", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="oauth provider filename")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="LDAP Provider Name")
@click.option("--url", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="LDAP URL with baseDN")
@click.option("--bind", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="Binding dn")
@click.option("--secret", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="LDAP secret")
@click.option("--id", is_flag=False, multiple=True, help="Attribute id")
@click.option("--name", is_flag=False, multiple=True, help="Attribute name")
@click.option("--username", is_flag=False, multiple=True, help="Attribute preferredUsername")
@click.option("--email", is_flag=False, multiple=True, help="Attribute email")
@click.option("--insecure", is_flag=True, show_default=True, default=False, help="LDAP secure mode")
@click.option("--mapping", type=click.Choice(['claim', 'lookup', 'add'], case_sensitive=False), default='claim', show_default=True, help="Mapping method")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_ldap_command(ctx, cluster_names, ldap_filename, provider_name, url, bind, secret, id, name, username, email, insecure, mapping, no_confirm):
    """Set identity ldap in openshift cluster"""

    task = {}
    task['feature'] = {}
    task['feature']['filename'] = ldap_filename
    task['feature']['provider'] = provider_name
    task['feature']['url'] = url
    task['feature']['bind'] = bind
    task['feature']['secret'] = secret
    task['feature']['id'] = id
    task['feature']['attribute_name'] = name
    task['feature']['username'] = username
    task['feature']['email'] = email
    task['feature']['mapping'] = mapping
    task['feature']['insecure'] = insecure

    success = ocp_common.set_workflow(cluster_names, 'identity-ldap', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)