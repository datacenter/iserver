import sys
import traceback
import click
from lib.workflow.ocp_ssh import create

from menu import validations
from menu import user_inputs


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("ssh")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--role", "node_role", type=click.Choice(['any', 'master', 'worker'], case_sensitive=False), default='any', show_default=True)
@click.option("--filename", multiple=True, help="SSH public key to be added")
@click.option("--no-wait", "no_wait", is_flag=True, show_default=True, default=False, help="No-wait for mcp update")
def set_ocp_ssh_command(
        ctx,
        cluster_name,
        node_role,
        filename,
        no_wait
        ):
    """Set ocp ssh authorized keys"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        if len(filename) == 0:
            item = user_inputs.get_value(ctx, prompt='SSH public key location')
            if len(item) == 0:
                raise ErrorExit
            
            filename = [item]

        params = {}
        params['cluster'] = cluster_name
        params['role'] = node_role
        params['filename'] = filename
        params['wait'] = not no_wait

        success = create.run(
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
