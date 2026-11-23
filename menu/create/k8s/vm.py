import sys
import click
from lib.workflow import ocp_common
from menu import validations


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--template", type=click.Choice(['generic', 'cirros'], case_sensitive=False), default='generic', help="Virtual machine template")
@click.option("--socket", type=click.INT, default=1, help="Socket count")
@click.option("--core", type=click.INT, default=1, help="Cores count")
@click.option("--thread", type=click.INT, default=1, help="Threads count")
@click.option("--memory", type=click.INT, help="Memory size in Gi")
@click.option("--network", multiple=True, help="Network configuration")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def create_k8s_vm_command(
        ctx,
        cluster_names,
        namespace,
        name,
        template,
        socket,
        core,
        thread,
        memory,
        network,
        no_wait,
        no_confirm
        ):
    """Create k8s vm"""

    task = {}
    task['vm'] = {}
    task['vm']['namespace'] = namespace
    task['vm']['name'] = name
    task['vm']['template'] = template
    task['vm']['socket'] = socket
    task['vm']['core'] = core
    task['vm']['thread'] = thread
    task['vm']['memory'] = memory
    task['vm']['network'] = network
    task['vm']['wait'] = not no_wait

    success = ocp_common.set_workflow(cluster_names, 'ocp-vm', task, not no_confirm, ctx.run_id)
    if not success:
        sys.exit(1)