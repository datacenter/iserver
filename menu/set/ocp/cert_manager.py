import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("cert-manager")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'issuer', 'crt'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="CRD namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="CRD name")
@click.option("--cn", default='', callback=validations.empty_string_to_none, help="Common name")
@click.option("--issuer", default='', callback=validations.empty_string_to_none, help="Issuer name")
@click.option("--crt", default='', callback=validations.empty_string_to_none, show_default=True, help="Certificate file")
@click.option("--key", default='', callback=validations.empty_string_to_none, show_default=True, help="Private key file")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cert_manager_command(ctx, cluster_names, mode, namespace, name, cn, issuer, crt, key, no_confirm):
    """Set cert manager in openshift cluster"""

    task = {}

    if mode in ['feature']:
        task['feature'] = {}

    if mode in ['issuer']:
        task['issuer'] = {}
        task['issuer']['namespace'] = namespace
        task['issuer']['name'] = name
        task['issuer']['crt'] = crt
        task['issuer']['key'] = key

    if mode in ['crt']:
        task['crt'] = {}
        task['crt']['namespace'] = namespace
        task['crt']['name'] = name
        task['crt']['cn'] = cn
        task['crt']['issuer'] = issuer

    success = ocp_common.set_workflow(cluster_names, 'cert-manager', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)