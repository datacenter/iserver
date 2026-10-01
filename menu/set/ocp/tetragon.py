import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("tetragon")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'crd'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--image", default='', callback=validations.empty_string_to_none, show_default=True, help="Tetragon Enterprise Operator image")
@click.option("--filename", multiple=True, help="Tetragon policy directory or file")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_tetragon_command(
        ctx,
        cluster_names,
        mode,
        channel,
        image,
        filename,
        no_confirm
    ):
    """Set tetragon enterprise operator in openshift cluster"""

    task = {}
    if mode in ['operator']:
        task['operator'] = {}
        task['operator']['channel'] = channel
        task['operator']['image'] = image

    if mode in ['crd']:
        task['crd'] = {}
        task['crd']['filename'] = []
        for item in filename:
            task['crd']['filename'].append(item)

    success = ocp_common.set_workflow(cluster_names, 'tetragon', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)