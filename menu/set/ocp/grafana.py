import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_grafana_operator import operator_create
from lib.workflow.ocp_prometheus import monitoring_enable
from lib.workflow.ocp_grafana_operator import instance_create
from lib.workflow.ocp_grafana_operator import dashboard_create

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("grafana")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'mon', 'instance', 'dashboard', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--instance", default='', callback=validations.empty_string_to_none, show_default=True, help="Grafana instance name")
@click.option("--username", default='root', callback=validations.empty_string_to_none, show_default=True, help="Grafana instance admin username")
@click.option("--password", default='root', callback=validations.empty_string_to_none, show_default=True, help="Grafana instance admin password")
@click.option("--prometheus", is_flag=True, show_default=True, default=False, help="Enable prometheus data source")
@click.option("--datasource", default='my-prometheus', show_default=True, help="Prometheus data source name")
@click.option("--crd", multiple=True, show_default=True, help="Grafana CRDs or template")
@click.option("--scope", multiple=True, show_default=True, help="Prometheus metric scope")
@click.option("--target", default='', callback=validations.empty_string_to_none, show_default=True, help="Target dashboard folder:name for template")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_grafana_command(ctx, cluster_name, mode, channel, instance, username, password, prometheus, datasource, crd, scope, target, no_confirm):
    """Set grafana operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['confirmation'] = not no_confirm
            
            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['mon', 'all']:
            if mode == 'all' and prometheus or mode == 'mon':
                params = {}
                params['cluster'] = cluster_name
                params['confirmation'] = not no_confirm
                
                success = monitoring_enable.run(
                    params,
                    log_id=ctx.run_id
                )
                if not success:
                    raise ErrorExit

        if mode in ['instance', 'all']:
            if mode == 'all' and instance is not None or mode == 'instance':
                if instance is None:
                    ctx.my_output.error('Define instance name')
                    raise ErrorExit
                
                params = {}
                params['cluster'] = cluster_name
                params['instance'] = instance
                params['username'] = username
                params['password'] = password
                params['prometheus'] = prometheus
                params['datasource'] = datasource
                params['confirmation'] = not no_confirm
                
                success = instance_create.run(
                    params,
                    log_id=ctx.run_id
                )
                if not success:
                    raise ErrorExit

        if mode in ['dashboard']:
            params = {}
            params['cluster'] = cluster_name
            params['instance'] = instance
            params['target'] = target
            params['crd'] = []
            for item in crd:
                params['crd'].append(item)
            params['scope'] = []
            for item in scope:
                params['scope'].append(item)

            params['confirmation'] = not no_confirm

            success = dashboard_create.run(
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
