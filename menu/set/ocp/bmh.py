import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_bare_metal_host import attach
from lib.workflow.ocp_bare_metal_host import create_host
from lib.workflow.ocp_bare_metal_host import enable
from lib.workflow.ocp_bare_metal_host import detach
from lib.workflow.ocp_bare_metal_host import inspect
from lib.workflow.ocp_bare_metal_host import power_on
from lib.workflow.ocp_bare_metal_host import power_off
from lib.workflow.ocp_bare_metal_host import reboot

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bmh")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
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
def set_ocp_bmh_command(ctx, cluster_name, mode, node, bmc, server_type, username, password, mac, serial, boot, cert, no_wait, no_confirm):
    """Set bare metal host in openshift cluster"""

    try:
        if mode == 'bmc':
            params = {}
            params['cluster'] = cluster_name
            params['bmc'] = []

            for item in bmc:
                if len(item.split(':')) != 2:
                    ctx.my_output.error('bmc node:address format required')
                    raise ErrorExit
                
                entry = {}
                entry['node'] = item.split(':')[0]
                entry['type'] = server_type
                entry['address'] = item.split(':')[1]
                entry['username'] = username
                entry['password'] = password
                entry['cert'] = cert
                params['bmc'].append(entry)

            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'node':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['bmc'] = None
            for item in bmc:
                params['bmc'] = item
                break

            params['type'] = server_type
            params['username'] = username
            params['password'] = password
            params['mac'] = mac
            params['serial'] = serial
            params['boot'] = boot
            params['cert'] = cert
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = create_host.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode == 'attach':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = attach.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'detach':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = detach.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'inspect':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = inspect.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
        if mode == 'on':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = power_on.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'off':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = power_off.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'reboot':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = reboot.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
            
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
