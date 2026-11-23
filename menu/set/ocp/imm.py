import sys
import click
from menu import defaults
from menu import validations
from lib.workflow import ocp_common


@click.command("imm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_imm_command(ctx, iaccount, cluster_names, no_confirm):
    """Set openshift cluster nodes to server mapping using Intersight"""

    task = {}
    task['configure'] = {}
    task['configure']['iaccount'] = iaccount

    success = ocp_common.set_workflow(cluster_names, 'imm', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)