import sys
import json
import threading
import traceback
import click

from lib.linux import output as linux_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("boot")
@click.pass_obj
@click.option("--server", default='', callback=validations.empty_string_to_none, help="Linux server name")
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_linux_boot_command(
        ctx,
        server,
        no_cache,
        output,
        devel
        ):
    """Get linux boot /proc/cmdline settings"""

    # iserver get linux boot

    ctx.developer = devel
    ctx.output = output

    try:
        linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
        linux_handler = validations.validate_linux_name(
            ctx,
            server,
            no_cache=no_cache
        )
        if linux_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        boot = linux_handler.get_boot()

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    boot,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(boot)

        linux_output_handler.print_linux_boot(
            boot
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
