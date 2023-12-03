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


@click.command("hp")
@click.pass_obj
@click.option("--server", multiple=True, help="Linux server name")
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_linux_hp_command(
        ctx,
        server,
        no_cache,
        output,
        devel
        ):
    """Get linux huge pages settings"""

    # iserver get linux hp

    ctx.developer = devel
    ctx.output = output

    try:
        linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
        linux_handlers = validations.validate_linux_names(
            ctx,
            server,
            no_cache=no_cache
        )
        if linux_handlers is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        for linux_handler in linux_handlers:
            if not linux_handler.ssh_handler.is_ssh():
                ctx.busy = False
                ctx.my_output.error(
                    'Linux server connection failed: %s' % (linux_handler.server_display_name)
                )
                raise ErrorExit

        huge_pages = []
        for linux_handler in linux_handlers:
            item = {}
            item['name'] = linux_handler.server_name
            item['hp'] = linux_handler.get_huge_pages()
            huge_pages.append(
                item
            )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    huge_pages,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(huge_pages)

        linux_output_handler.print_linux_huge_pages(
            huge_pages,
            title=True
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
