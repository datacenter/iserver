import sys
import click
from menu import validations
from lib.workflow import ocp_common


@click.command("grafana")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
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
def set_ocp_grafana_command(ctx, cluster_names, mode, channel, instance, username, password, prometheus, datasource, crd, scope, target, no_confirm):
    """Set grafana operator in openshift cluster"""

    task = {}

    if mode in ['operator', 'all']:
        task['operator'] = {}
        task['operator']['channel'] = channel

    if mode in ['instance', 'all']:
        if mode == 'all' and instance is not None or mode == 'instance':
            task['instance'] = {}
            task['instance']['instance'] = instance
            task['instance']['username'] = username
            task['instance']['password'] = password
            task['instance']['prometheus'] = prometheus
            task['instance']['datasource'] = datasource

    if mode in ['dashboard']:
        task['dashboard'] = {}
        task['dashboard']['instance'] = instance
        task['dashboard']['target'] = target
        task['dashboard']['crd'] = crd
        task['dashboard']['scope'] = scope

    if mode in ['mon', 'all']:
        if mode == 'all' and prometheus or mode == 'mon':
            task['mon'] = {}

    success = ocp_common.set_workflow(cluster_names, 'grafana', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)