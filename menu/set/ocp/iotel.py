import sys
import click
from menu import defaults
from menu import validations
from lib.workflow import ocp_common


@click.command("iotel")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['instance', 'poller'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--iaccount", default='', callback=validations.empty_string_to_none, help="Intersight account")
@click.option("--key", default='', callback=validations.empty_string_to_none, help="Intersight key id")
@click.option("--pem", default='', callback=validations.empty_string_to_none, help="Intersight pem filename")
@click.option("--suffix", default='', callback=validations.empty_string_to_none, help="Resources name suffix")
@click.option("--pollers", default='', callback=validations.empty_string_to_none, help="Pollers definition file")
@click.option("--dir", default='', callback=validations.empty_string_to_none, help="Template directory")
@click.option("--template", "ptemplate", multiple=True, help="Poller template")
@click.option("--target", "ptarget", multiple=True, help="Target server")
@click.option("--attribute", "pattribute", multiple=True, help="Extra metric attributes")
@click.option("--pmode", type=click.Choice(['add', 'set'], case_sensitive=False), default='add', show_default=True, help="Pollers modification mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_iotel_command(ctx, cluster_names, mode, iaccount, key, pem, suffix, pollers, dir, ptemplate, ptarget, pattribute, pmode, no_confirm):
    """Set openshift intersight open telemetry collector"""


    task = {}

    if mode in ['instance']:
        task['instance'] = {}
        task['instance']['iaccount'] = iaccount
        task['instance']['key'] = key
        task['instance']['pem'] = pem
        task['instance']['suffix'] = suffix
        task['instance']['pollers'] = pollers

    if mode in ['poller']:
        task['poller'] = {}
        task['poller']['suffix'] = suffix
        task['poller']['pollers'] = pollers
        task['poller']['dir'] = dir
        task['poller']['mode'] = pmode
        task['poller']['template'] = ptemplate
        task['poller']['target'] = ptarget
        task['poller']['attribute'] = pattribute

    success = ocp_common.set_workflow(cluster_names, 'iotel', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)