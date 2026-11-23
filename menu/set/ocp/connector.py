import sys
import click
from menu import validations
from lib.workflow import ocp_common



@click.command("connector")
@click.pass_obj
@click.option("--cluster", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Domain name")
@click.option("--kubeconfig", "kubeconfig_filename", default='', callback=validations.empty_string_to_none, help="Kubeconfig filename")
@click.option("--ssh", "ssh_public_key", default='', callback=validations.empty_string_to_none, help="SSH public key filename")
@click.option("--mgmt", "management_ip", default='', callback=validations.empty_string_to_none, help="Management IP")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_connector(
        ctx,
        cluster,
        domain_name,
        kubeconfig_filename,
        ssh_public_key,
        management_ip,
        no_confirm
        ):
    """Set ocp cluster connector"""

    if cluster is None:
        ctx.my_output.error('Define cluster connector name')
        sys.exit(1)

    task = {}
    task['set'] = {}
    task['set']['domain'] = domain_name
    task['set']['kubeconfig_filename'] = kubeconfig_filename
    task['set']['ssh_public_key_filename'] = ssh_public_key
    task['set']['management_ip'] = management_ip

    success = ocp_common.set_workflow([cluster], 'ocp-connector', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)