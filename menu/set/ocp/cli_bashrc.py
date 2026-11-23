import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("cli-bashrc")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--http_proxy", default='', callback=validations.empty_string_to_none, help="http proxy")
@click.option("--https_proxy", default='', callback=validations.empty_string_to_none, help="https proxy")
@click.option("--no_proxy", default='', callback=validations.empty_string_to_none, help="no proxy")
@click.option("--inherit", is_flag=True, show_default=True, default=False, help="Inherit from cluster proxy")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cli_bashrc_command(
        ctx,
        cluster_names,
        http_proxy,
        https_proxy,
        no_proxy,
        inherit,
        no_confirm
        ):
    """Set ocp cluster bashrc proxy settings"""

    task = {}
    task['bashrc'] = {}
    task['bashrc']['http_proxy'] = http_proxy
    task['bashrc']['https_proxy'] = https_proxy
    task['bashrc']['no_proxy'] = no_proxy
    task['bashrc']['inherit'] = inherit

    success = ocp_common.set_workflow(cluster_names, 'cli', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)