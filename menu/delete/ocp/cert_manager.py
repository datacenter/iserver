import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cert-manager")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['feature', 'issuer', 'crt', 'wipe'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="CRD namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="CRD name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cert_manager_command(ctx, cluster_names, mode, namespace, name, no_confirm):
    """Delete cert manager from openshift cluster"""

    task = {}

    if mode in ['feature']:
        task['feature'] = {}

    if mode in ['issuer']:
        task['issuer'] = {}
        task['issuer']['namespace'] = namespace
        task['issuer']['name'] = name

    if mode in ['crt']:
        task['crt'] = {}
        task['crt']['namespace'] = namespace
        task['crt']['name'] = name

    if mode in ['wipe']:
        task['wipe'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'cert-manager', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)