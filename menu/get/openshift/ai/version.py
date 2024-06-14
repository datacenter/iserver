import sys
import traceback
import json
import threading
import click

from lib.openshift import console
from lib.openshift import output as openshift_output

from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("version")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_openshift_ai_version_command(
        ctx,
        output,
        devel
        ):
    """Get openshift assisted installer supported versions"""

    ctx.developer = devel
    ctx.output = output

    try:
        openshift_output_handler = openshift_output.OpenshiftOutput(log_id=ctx.run_id)
        console_handler = console.Console(log_id=ctx.run_id)

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        versions = console_handler.get_assisted_install_versions()

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    versions,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(versions)

        openshift_output_handler.print_assisted_install_versions(
            versions['openshift'],
            title=True
        )

        ctx.my_output.default('The latest production version: %s' % (console_handler.get_assisted_install_versions_latest()))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
