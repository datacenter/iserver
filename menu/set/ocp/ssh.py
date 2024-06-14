import sys
import traceback
import click

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--action", type=click.Choice(['add', 'del'], case_sensitive=False))
@click.option("--file", "filename", default='', callback=validations.validate_optional_file, help="SSH public key to be added")
@click.option("--key", default='', help="SSH public key search pattern to be removed")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for mcp update")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ocp_ssh_command(
        ctx,
        cluster_name,
        node_role,
        action,
        filename,
        key,
        no_wait,
        devel
        ):
    """Set ocp ssh authorized keys"""

    # iserver set ocp ssh

    ctx.developer = devel
    ctx.output = 'default'

    try:
        if action is None or action not in ['add', 'del']:
            ctx.my_output.error('--action add|del required')
            raise ErrorExit

        if action == 'add':
            if filename is None:
                ctx.my_output.error('Filename with ssh public key required')
                raise ErrorExit

        if action == 'del':
            if len(key) == 0:
                ctx.my_output.error('SSH public key search pattern required')
                raise ErrorExit

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        ctx.my_output.default('Checking machine config pools...')
        machine_config_pools = ocp_handler.k8s_handler.get_machine_config_pools()

        if not ocp_handler.k8s_handler.is_machine_config_pools_ready(machine_config_pools=machine_config_pools):
            ctx.my_output.error('Machine config pools are not ready for new configuration')
            raise ErrorExit

        ctx.my_output.default('Machine config pools ready for new configuration')

        if action == 'add':
            machine_configs = ocp_handler.add_ocp_ssh_authorized_key(
                filename,
                node_role
            )

        if action == 'del':
            machine_configs = ocp_handler.delete_ocp_ssh_authorized_key(
                key,
                node_role
            )

        if machine_configs is None:
            ctx.my_output.error(
                'Failed to set ssh authorized key'
            )
            raise ErrorExit

        if len(machine_configs) == 0:
            ctx.my_output.default('Completed (no change)')

        if len(machine_configs) > 0:
            ctx.my_output.default('Completed with machine configs modified')
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
