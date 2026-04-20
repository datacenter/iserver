import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_bare_metal_host import delete_host

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bmh")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['node'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--node", default='', callback=validations.empty_string_to_none, show_default=True, help="Host name")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
def delete_ocp_bmh_command(ctx, cluster_name, mode, node, no_wait):
    """Set bare metal host in openshift cluster"""

    try:
        if mode == 'node':
            params = {}
            params['cluster'] = cluster_name
            params['node'] = node
            params['wait'] = not no_wait

            success = delete_host.run(
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
