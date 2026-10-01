import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("tetragon")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'crd', 'wipe', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--filename", multiple=True, show_default=True, help="Tetragon policy directory or file")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_tetragon_command(ctx, cluster_names, mode, filename, no_confirm):
    """Delete tetragon operator in openshift cluster"""

    task = {}
    if mode in ['operator', 'all']:
        task['operator'] = {}

    if mode in ['crd']:
        task['crd'] = {}
        task['crd']['filename'] = []
        for item in filename:
            task['crd']['filename'].append(item)

    if mode in ['wipe', 'all']:
        task['wipe'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'tetragon', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)