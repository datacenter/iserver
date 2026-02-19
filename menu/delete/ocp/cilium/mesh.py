import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_mesh import feature_disable
from lib.workflow.ocp_cilium_mesh import cluster_delete
from lib.workflow.ocp_cilium_mesh import timescape_disable


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("mesh")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['feature', 'cluster', 'timescape'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--mesh-name", default='', callback=validations.empty_string_to_none, help="Cluster mesh name")
@click.option("--mesh-ip", default='', callback=validations.validate_ip, help="Cluster mesh ip")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_cilium_mesh_command(ctx, cluster_name, mode, mesh_name, mesh_ip, no_confirm):
    """Delete cilium cluster mesh"""

    try:
        if mode in ['feature']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = feature_disable.run(
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
            params['confirmation'] = not no_confirm

            success = cluster_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit         

        if mode in ['timescape']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = timescape_disable.run(
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
