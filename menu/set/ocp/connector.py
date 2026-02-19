import sys
import traceback
import click

from lib.workflow.ocp_access import set as ocp_workflow

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("connector")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="OCP cluster name")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Domain name")
@click.option("--kubeconfig", "kubeconfig_filename", default='', callback=validations.empty_string_to_none, help="Kubeconfig filename")
@click.option("--ssh", "ssh_public_key", default='', callback=validations.empty_string_to_none, help="SSH public key filename")
@click.option("--mgmt", "management_ip", default='', callback=validations.empty_string_to_none, help="Management IP")
def set_ocp_connector(
        ctx,
        cluster_name,
        domain_name,
        kubeconfig_filename,
        ssh_public_key,
        management_ip
        ):
    """Set ocp cluster connector"""

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['domain'] = domain_name
        params['kubeconfig_filename'] = kubeconfig_filename
        params['ssh_public_key_filename'] = ssh_public_key
        params['management_ip'] = management_ip

        success = ocp_workflow.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit
        
    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
