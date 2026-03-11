import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_identity_ldap import add as ocp_add_workflow
from menu import user_inputs


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ldap")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
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
def set_ocp_ldap_command(ctx, cluster_name, ldap_filename, provider_name, url, bind, secret, id, name, username, email, insecure, mapping, no_confirm):
    """Set identity ldap in openshift cluster"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['filename'] = ldap_filename
        params['provider'] = provider_name
        params['url'] = url
        params['bind'] = bind
        params['secret'] = secret
        params['id'] = []
        for item in id:
            params['id'].append(item)
        params['attribute_name'] = []
        for item in name:
            params['attribute_name'].append(item)
        params['username'] = []
        for item in username:
            params['username'].append(item)
        params['email'] = []
        for item in email:
            params['email'].append(item)
        params['mapping'] = mapping
        params['insecure'] = insecure
        params['confirmation'] = not no_confirm

        success = ocp_add_workflow.run(
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
