import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("csr")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="CSR name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_csr_command(
        ctx, 
        cluster_names,
        name,
        no_wait,
        no_confirm
    ):
    """Approve certificate signing request"""

    task = {}
    task['csr'] = {}
    task['csr']['name'] = name
    task['csr']['wait'] = not no_wait

    success = ocp_common.set_workflow(cluster_names, 'adm', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)