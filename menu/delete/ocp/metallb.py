import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("metallb")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all', 'pool', 'peer', 'community', 'adv', 'bfd', 'wipe', 'nuke'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--pool", default='', callback=validations.empty_string_to_none, show_default=True, help="IP address pool name")
@click.option("--peer", default='', callback=validations.empty_string_to_none, show_default=True, help="BGP peer name")
@click.option("--community", default='', callback=validations.empty_string_to_none, show_default=True, help="Community name")
@click.option("--adv", default='', callback=validations.empty_string_to_none, show_default=True, help="Advertisement name")
@click.option("--bfd", default='', callback=validations.empty_string_to_none, show_default=True, help="BFD profile name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_metallb_command(ctx, cluster_names, mode, pool, peer, community, adv, bfd, no_confirm):
    """Delete metallb operator in openshift cluster"""

    if mode in ['wipe', 'nuke']:
        pool = '__all__'
        peer = '__all__'
        community = '__all__'
        adv = '__all__'
        bfd = '__all__'

    task = {}

    if mode in ['peer', 'wipe', 'nuke']:
        task['peer'] = {}
        task['peer']['peer'] = peer

    if mode in ['community', 'wipe', 'nuke']:
        task['community'] = {}
        task['community']['community'] = community

    if mode in ['adv', 'wipe', 'nuke']:
        task['adv'] = {}
        task['adv']['advertisement'] = adv

    if mode in ['bfd', 'wipe', 'nuke']:
        task['bfd'] = {}
        task['bfd']['bfd'] = bfd

    if mode in ['bfd', 'wipe', 'nuke']:
        task['pool'] = {}
        task['pool']['pool'] = pool
        
    if mode in ['instance', 'all', 'nuke']:
        task['instance'] = {}

    if mode in ['operator', 'all', 'nuke']:
        task['operator'] = {}

    success = ocp_common.delete_workflow(cluster_names, 'metallb', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)