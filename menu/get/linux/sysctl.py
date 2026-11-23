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


@click.command("sysctl")
@click.pass_obj
@click.option("--server", default='', callback=validations.empty_string_to_none, help="Linux server name")
@click.option("--key", default='', callback=validations.empty_string_to_none, help="Filter by parameter name")
@click.option("--diff", "candidate_diff_servers", multiple=True, default=[], help="Diff server name")
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_linux_sysctl_command(
        ctx,
        server,
        key,
        candidate_diff_servers,
        no_cache,
        output,
        devel
        ):
    """Get linux sysctl parameters"""

    # iserver get linux sysctl

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

        diff_handlers = {}
        diff_servers = []
        if len(candidate_diff_servers) > 0:
            for candidate_diff_server in candidate_diff_servers:
                diff_handler = validations.validate_linux_name(
                    ctx,
                    candidate_diff_server,
                    no_cache=no_cache
                )
                if diff_handler is None:
                    raise ErrorExit

                diff_handlers[diff_handler.server_name] = diff_handler
                diff_servers.append(
                    diff_handler.server_name
                )

        sysctl_filter = []
        if key is not None:
            sysctl_filter.append(
                'key:%s' % (key)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        sysctl = linux_handler.get_sysctl(sysctl_filter=sysctl_filter)
        diff_sysctl = {}
        for diff_server in diff_servers:
            diff_sysctl[diff_server] = diff_handlers[diff_server].get_sysctl(sysctl_filter=sysctl_filter)

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    sysctl,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(sysctl)

        linux_output_handler.print_linux_sysctl(
            sysctl,
            diff_servers,
            diff_sysctl,
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
