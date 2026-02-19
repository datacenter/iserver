import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_iotel import instance_delete
from lib.workflow.ocp_iotel import poller_delete


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("iotel")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['instance', 'poller'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--suffix", default='', callback=validations.empty_string_to_none, help="Suffix name")
@click.option("--metric", multiple=True, help="Metric name")
@click.option("--attribute", multiple=True, help="Metric name")
@click.option("--wipe", is_flag=True, show_default=True, default=False, help="Wipe mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_iotel_command(ctx, cluster_name, mode, suffix, metric, attribute, wipe, no_confirm):
    """Delete openshift intersight open telemetry collector"""

    try:
        if mode == 'instance':
            params = {}
            params['cluster'] = cluster_name
            params['suffix'] = suffix
            params['wipe'] = wipe

            success = instance_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'poller':
            params = {}
            params['cluster'] = cluster_name
            params['suffix'] = suffix
            params['metric'] = []
            for item in metric:
                params['metric'].append(item)
            params['attribute'] = []
            for item in attribute:
                params['attribute'].append(item)
            params['confirmation'] = not no_confirm

            success = poller_delete.run(
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
