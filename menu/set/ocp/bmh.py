import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("bmh")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--mode", type=click.Choice(['node', 'bmc', 'attach', 'detach', 'inspect', 'on', 'off', 'reboot'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Node name or __all__")
@click.option("--bmc", is_flag=False, multiple=True, help="node:address")
@click.option("--type", "server_type", type=click.Choice(['ucsc'], case_sensitive=False), default='ucsc', show_default=True, help="server type")
@click.option("--username", default='', callback=validations.empty_string_to_none, show_default=True, help="bmc username")
@click.option("--password", default='', callback=validations.empty_string_to_none, show_default=True, help="bmc password")
@click.option("--mac", default='', callback=validations.empty_string_to_none, show_default=True, help="Boot mac address")
@click.option("--serial", default='', callback=validations.empty_string_to_none, show_default=True, help="Serial number")
@click.option("--boot", type=click.Choice(['uefi', 'secure', 'legacy'], case_sensitive=False), default='uefi', show_default=True, help="Boot mode")
@click.option("--cert", is_flag=True, show_default=True, default=False, help="Certificate mode")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_bmh_command(ctx, cluster_names, mode, node, bmc, server_type, username, password, mac, serial, boot, cert, no_wait, no_confirm):
    """Set bare metal host in openshift cluster"""

    task = {}
    if mode in ['bmc']:
        task['register'] = {}
        task['register']['bmc'] = []
        for item in bmc:
            if len(item.split(':')) != 2:
                ctx.my_output.error('bmc node:address format required')
                sys.exit(1)
            
            entry = {}
            entry['node'] = item.split(':')[0]
            entry['type'] = server_type
            entry['address'] = item.split(':')[1]
            entry['username'] = username
            entry['password'] = password
            entry['cert'] = cert
            task['register']['bmc'].append(entry)

        task['register']['wait'] = not no_wait

    if mode in ['node']:
        task['node'] = {}
        task['node']['node'] = node
        task['node']['bmc'] = bmc
        task['node']['type'] = server_type
        task['node']['username'] = username
        task['node']['password'] = password
        task['node']['mac'] = mac
        task['node']['serial'] = serial
        task['node']['boot'] = boot
        task['node']['cert'] = cert
        task['node']['wait'] = not no_wait

    if mode in ['attach']:
        task['attach'] = {}
        task['attach']['node'] = node
        task['attach']['wait'] = not no_wait

    if mode in ['detach']:
        task['detach'] = {}
        task['detach']['node'] = node
        task['detach']['wait'] = not no_wait

    if mode in ['inspect']:
        task['inspect'] = {}
        task['inspect']['node'] = node
        task['inspect']['wait'] = not no_wait

    if mode in ['on']:
        task['power-on'] = {}
        task['power-on']['node'] = node
        task['power-on']['wait'] = not no_wait

    if mode in ['off']:
        task['power-off'] = {}
        task['power-off']['node'] = node
        task['power-off']['wait'] = not no_wait

    if mode in ['reboot']:
        task['reboot'] = {}
        task['reboot']['node'] = node
        task['reboot']['wait'] = not no_wait

    success = ocp_common.set_workflow(cluster_names, 'bmh', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)