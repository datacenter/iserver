import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("metallb")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'all', 'pool', 'peer', 'community', 'adv', 'bfd'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--filename", default='', callback=validations.validate_k8s_yaml_file_optional, show_default=True, help="MetalLB CRD")
@click.option("--bgp", type=click.Choice(['', 'native', 'frr', 'frr-k8s'], case_sensitive=False), default='native', show_default=True, help="BGP backend")
@click.option("--pool", default='', callback=validations.empty_string_to_none, show_default=True, help="IP address pool name")
@click.option("--addr", multiple=True, help="Address pool")
@click.option("--community", multiple=True, help="Community")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_metallb_command(ctx, cluster_names, mode, channel, filename, bgp, pool, addr, community, no_confirm):
    """Set metallb operator in openshift cluster"""

    task = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['instance', 'all']:
        task['instance'] = {}
        task['instance']['filename'] = filename
        task['instance']['bgp'] = bgp

    if mode in ['pool']:
        task['pool'] = {}
        task['pool']['pool'] = pool
        task['pool']['addr'] = addr

    if mode in ['peer']:
        task['peer'] = {}

    if mode in ['community']:
        task['community'] = {}
        task['community']['community'] = community

    if mode in ['adv']:
        task['adv'] = {}

    if mode in ['bfd']:
        task['bfd'] = {}

    success = ocp_common.set_workflow(cluster_names, 'metallb', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)