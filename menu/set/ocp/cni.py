import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cni import migrate


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cni")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['cilium'], case_sensitive=False), default='', show_default=True, help="Target cni")
@click.option("--cidr", default='', callback=validations.validate_ip_subnet, help="Target cidr")
@click.option("--host-prefix", default=24, type=click.INT, show_default=True, help="Target host prefix")
@click.option("--manifest", default='', callback=validations.validate_directory, help="Manifest directory")
@click.option("--start", default=1, type=click.INT, show_default=True, help="Starting step")
@click.option("--stop", default=10, type=click.INT, show_default=True, help="Ending step")
@click.option("--no-reload", is_flag=True, show_default=True, default=False, help="Disable auto-reload in case of failed mcp-triggered restart")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cni_command(
        ctx, 
        cluster_name, 
        mode,
        cidr,
        host_prefix,
        manifest,
        start,
        stop,
        no_reload,
        no_confirm
    ):
    """Set openshift data foundation operator in openshift cluster"""

    try:
        if mode in ['cilium']:
            params = {}
            params['cluster'] = cluster_name
            params['cidr'] = cidr
            params['host_prefix'] = host_prefix
            params['manifest'] = manifest
            params['start'] = start
            params['stop'] = stop
            params['reload'] = not no_reload
            params['confirmation'] = not no_confirm

            success = migrate.run(
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
