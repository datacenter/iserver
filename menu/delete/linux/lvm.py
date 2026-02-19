import sys
import traceback
import click

from lib.workflow.linux_lvm import wipe
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("lvm")
@click.pass_obj
@click.option("--server", multiple=True, help="Linux server name")
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_linux_lvm_command(
        ctx,
        server,
        no_cache,
        output,
        devel
        ):
    """Get lvm"""

    ctx.developer = devel
    ctx.output = output

    try:
        linux_handlers = validations.get_linux_handlers(
            ctx,
            server,
            no_cache=no_cache
        )
        if linux_handlers is None:
            raise ErrorExit

        for name in linux_handlers:
            wipe.run(
                linux_handlers[name],
                ctx.my_output,
                server_name=name
            )

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
