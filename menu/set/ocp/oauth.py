import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("oauth")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['log', 'restart'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--scope", type=click.Choice(['oauth', 'operator'], case_sensitive=False), default='oauth', show_default=True, help="Restart deployment")
@click.option("--level", type=click.Choice(['Normal', 'Debug', 'Trace', 'TraceAll'], case_sensitive=False), default='Normal', show_default=True, help="Debug level")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_oauth_command(
        ctx,
        cluster_names,
        mode,
        scope,
        level,
        no_confirm
    ):
    """Set authantication in openshift cluster"""

    task = {}

    if mode in ['log']:
        task['log'] = {}
        task['log']['level'] = level

    if mode in ['restart']:
        task['restart'] = {}
        task['restart']['scope'] = scope

    success = ocp_common.set_workflow(cluster_names, 'oauth', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)