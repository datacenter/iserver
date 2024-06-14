import sys
import json
import threading
import traceback
import click

from lib.iwo import main as iwo

from menu import validations
from menu import defaults
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("volume")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_iwo_volume_command(
        ctx,
        iaccount,
        output,
        verbose,
        debug,
        devel
        ):
    """Get iwo volume"""

    # iserver get iwo volume

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        iwo_handler = iwo.Iwo(
            iaccount,
            verbose=verbose,
            debug=debug,
            log_id=ctx.run_id
        )

        managed_objects = iwo_handler.get_volumes()
        if managed_objects is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get volume')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    managed_objects,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(managed_objects)

        iwo_handler.print_volumes(managed_objects)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
