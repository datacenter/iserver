import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_ssh import delete


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--filename", multiple=True, help="SSH public key to be deleted")
@click.option("--key", multiple=True, help="SSH public key search pattern to be removed")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for mcp update")
def delete_ocp_ssh_command(
        ctx,
        cluster_name,
        node_role,
        filename,
        key,
        no_wait
        ):
    """Delete ocp ssh authorized keys"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        params = {}
        params['cluster'] = cluster_name
        params['role'] = node_role
        params['filename'] = filename
        params['key'] = key
        params['wait'] = not no_wait

        success = delete.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
