import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_mesh import feature_enable
from lib.workflow.ocp_cilium_mesh import cluster_create
from lib.workflow.ocp_cilium_mesh import timescape_enable


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("mesh")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['feature', 'cluster', 'timescape'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--mesh-id", default=0, type=click.INT, help="Cluster mesh id")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--mesh-ip", default='', callback=validations.validate_ip, help="Cluster mesh ip address")
@click.option("--mesh-port", type=click.INT, help="Cluster mesh port")
@click.option("--ca-crt", default='', callback=validations.empty_string_to_none, show_default=True, help="Root ca crt")
@click.option("--ca-key", default='', callback=validations.empty_string_to_none, show_default=True, help="Root ca key")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for cluster mesh up")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_cilium_mesh_command(ctx, cluster_name, mode, mesh_id, mesh_name, mesh_ip, mesh_port, ca_crt, ca_key, no_wait, no_confirm):
    """Set cilium cluster mesh"""

    try:
        if mode in ['feature']:
            params = {}
            params['cluster'] = cluster_name
            params['mesh-id'] = mesh_id
            params['mesh-name'] = mesh_name
            params['mesh-port'] = mesh_port
            params['ca-crt'] = ca_crt
            params['ca-key'] = ca_key
            params['confirmation'] = not no_confirm

            success = feature_enable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit         

        if mode in ['cluster']:
            params = {}
            params['cluster'] = cluster_name
            params['mesh-name'] = mesh_name
            params['mesh-ip'] = mesh_ip
            params['mesh-port'] = mesh_port
            params['wait'] = not no_wait
            params['confirmation'] = not no_confirm

            success = cluster_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit  

        if mode in ['timescape']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = timescape_enable.run(
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
