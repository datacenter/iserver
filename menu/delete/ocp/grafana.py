import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_grafana_operator import operator_delete
from lib.workflow.ocp_prometheus import monitoring_disable
from lib.workflow.ocp_grafana_operator import instance_delete
from lib.workflow.ocp_grafana_operator import wipe

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("grafana")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'mon', 'instance', 'wipe', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--instance", default='', callback=validations.empty_string_to_none, show_default=True, help="Grafana instance name")
def delete_ocp_grafana_command(ctx, cluster_name, mode, instance):
    """Delete grafana operator in openshift cluster"""

    try:
        if mode == 'instance':
            params = {}
            params['cluster'] = cluster_name
            params['instance'] = instance

            success = instance_delete.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['wipe', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = wipe.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['mon', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = monitoring_disable.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name

            success = operator_delete.run(
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
