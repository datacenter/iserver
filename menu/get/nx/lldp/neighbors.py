import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("neighbors")
@click.pass_obj
@click.option("--switch", "switch", default='', callback=validations.validate_nexus_name, help="Switch name")
@click.option("--ip", "switch_ip", default='', callback=validations.validate_ip, help="Switch IP")
@click.option("--username", "switch_username", default='', help="Switch Username")
@click.option("--password", "switch_password", default='', help="Switch Password")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nx_lldp_neighbors_command(
        ctx,
        switch,
        switch_ip,
        switch_username,
        switch_password,
        output,
        devel
        ):
    """Get nx lldp neighbors"""

    # iserver get nx lldp neighbors

    ctx.developer = devel
    ctx.output = output

    try:
        nexus_handler = validations.validate_nexus_switch(
            ctx,
            switch,
            switch_ip,
            switch_username,
            switch_password
        )
        if nexus_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        neighbors = nexus_handler.get_lldp_neighbors()

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    neighbors,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(neighbors)

        nexus_handler.print_lldp_neighbors(
            neighbors
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
