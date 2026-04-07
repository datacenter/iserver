import sys
import traceback
import click
from lib.workflow.ocp_ovn_bgp import feature_disable
from lib.workflow.ocp_ovn_bgp import ra_disable
from lib.workflow.ocp_ovn_bgp import configuration_delete
from lib.workflow.ocp_ovn_bgp import ra_delete
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ovn-bgp")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['feature', 'ra', 'all', 'config', 'ra-config'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--config", default='', callback=validations.empty_string_to_none, show_default=True, help="FRR configuration name")
def delete_ocp_ovn_bgp(
        ctx,
        cluster_name,
        mode,
        config
        ):
    """Delete ocp cluster ovn bgp"""

    ctx.developer = False

    try:
        if mode in ['ra', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = ra_disable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['feature', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = feature_disable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'config':
            params = {}
            params['cluster'] = cluster_name
            params['config'] = config
            
            success = configuration_delete.run(
                params,
                log_id=ctx.run_id
            )

        if mode == 'ra-config':
            params = {}
            params['cluster'] = cluster_name
            params['config'] = config
            
            success = ra_delete.run(
                params,
                log_id=ctx.run_id
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
