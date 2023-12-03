import sys
import traceback
import threading
import click

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--file", "filename", default='', callback=validations.validate_file, help="SSH public key")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for mcp update")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_ocp_ssh_command(
        ctx,
        cluster_name,
        node_role,
        filename,
        no_wait,
        devel
        ):
    """Create ocp ssh authorized keys"""

    # iserver create ocp ssh

    ctx.developer = devel
    ctx.output = 'default'

    try:
        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        machine_config_pools = ocp_handler.k8s_handler.get_machine_config_pools()
        machine_configs = ocp_handler.add_ocp_ssh_authorized_key(
            filename,
            node_role
        )

        ctx.busy = False

        if machine_configs is None:
            ctx.my_output.error(
                'Failed to set ssh authorized key'
            )
            raise ErrorExit

        if len(machine_configs) == 0:
            ctx.my_output.default('Completed (no change)')
            return

        ctx.my_output.default('Completed with machine configs modifed')
        for machine_config in machine_configs:
            ctx.my_output.default('- %s' % (machine_config))

        if no_wait:
            return

        if not ocp_handler.k8s_handler.wait_machine_config_pool_update(machine_config_pools, machine_configs, output_handler=ctx.my_output):
            raise ErrorExit

        ctx.my_output.default('Completed')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
