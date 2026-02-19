import sys
import json
import threading
import traceback
import click

from lib.cnc import output as cnc_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("node")
@click.pass_obj
@click.option("--cnc", "controller", default='', callback=validations.validate_cnc_name, help="CNC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="CNC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="CNC Port")
@click.option("--username", "controller_username", default='', help="CNC Username")
@click.option("--password", "controller_password", default='', help="CNC Password")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--ttl", "requested_ttl", default=-1, show_default=True, help="Cache ttl")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_cnc_node_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        view,
        output,
        requested_ttl,
        devel
        ):
    """Get cnc node"""

    # iserver get cnc node

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state',
        'state',
        []
    )

    try:
        cnc_output_handler = cnc_output.CncOutput(log_id=ctx.run_id)
        cnc_handler = validations.validate_cnc_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            requested_ttl=requested_ttl
        )
        if cnc_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        nodes = cnc_handler.get_nodes()
        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    nodes,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(nodes)

        if 'state' in view:
            cnc_output_handler.print_nodes(
                nodes,
                title=True
            )

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   state (def)')

        if len(nodes) == 0:
            raise NoResultExit

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
