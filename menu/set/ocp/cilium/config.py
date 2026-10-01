import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("config")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--filename", default='', callback=validations.empty_string_to_none, show_default=True, help="Target configuration")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-rollback", "no_rollback", is_flag=True, show_default=True, default=False, help="Rollback mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_config_command(ctx, cluster_names, filename, no_wait, no_confirm, no_rollback):
    """Set cilium configuration"""

    task = {}
    task['configure'] = {}
    task['configure']['filename'] = filename
    task['configure']['wait'] = not no_wait
    task['configure']['rollback'] = not no_rollback

    success = ocp_common.set_workflow(cluster_names, 'cilium', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)